"""Contains async functions to extract and parse the status of the apcupsd NIS."""
from __future__ import annotations

import asyncio
from collections import OrderedDict

_STATUS_CMD = b"\x00\x06status"
_EOF = b"\x00\x00"

UNITS = {
    "Minutes",
    "Seconds",
    "Percent",
    "Volts",
    "Watts",
    "Amps",
    "Hz",
    "C",
    # APCUPSd reports data for "itemp" field (eventually represented by UPS Internal Temperature
    # sensor in this integration) with a trailing "Internal", e.g., "34.6 C Internal". Here we
    # create a fake unit " C Internal" to handle this case.
    "C Internal",
    "VA",
    "Percent Load Capacity",
    # "stesti" field (Self Test Interval) field could report a "days" unit, e.g., "7 days", so here
    # we add support for it.
    "days",
}


async def request_status(
    host: str = "localhost",
    port: int = 3551,
) -> OrderedDict[str, str]:
    """Connect to the APCUPSd NIS and request its status and return the parsed dict.

    :param host: the host which apcupsd is listening on.
    :param port: the port which apcupsd is listening on.
    :return: an ordered dict, where key is the field (e.g., "NOMINV") and value is the
    value. For example, {"NOMINV": "12.0 Volts", ..., "SERIALNO": "XXXXXXX"}
    """
    return parse_raw_status(await request_raw_status(host, port))


def parse_raw_status(raw_status: bytes) -> OrderedDict[str, str]:
    """Parse the raw status and return an ordered dict.

    :param raw_status: raw status string retrieved from apcupsd.
    :return: an ordered dict, where key is the field (e.g., "NOMINV") and value is the
    value. For example, {"NOMINV": "12.0 Volts", ..., "SERIALNO": "XXXXXXX"}
    """
    result = OrderedDict()

    # Strip EOF from the status and decode to string.
    if not raw_status.endswith(_EOF):
        raise ValueError("raw status does not end with EOF")
    status = raw_status[: -len(_EOF)].decode()

    # An example line is like this:
    # "<LENGTH_BYTE>DATE     : 1970-01-01 00:00:00 -0000  \n\x00",
    # where "<LENGTH_BYTE>" is one byte that indicates the length of the line.

    # Therefore, we first split by the line separator "\x00".
    # Each line will look like:
    # "<LENGTH_BYTE>DATE     : 1970-01-01 00:00:00 -0000  \n".
    for line in status.split("\x00"):
        if len(line) == 0:
            continue

        # Strip the length byte
        # "DATE     : 1970-01-01 00:00:00 -0000  \n".
        line = line[1:]

        # Split by ":" once
        # ("DATE     ", " 1970-01-01 00:00:00 -0000  \n").
        name, value = line.split(":", maxsplit=1)
        # Strip spaces and newlines
        # ("DATE", "1970-01-01 00:00:00 -0000")
        name, value = name.strip(), value.strip()
        result[name] = value

    return result


async def request_raw_status(host: str = "localhost", port: int = 3551) -> bytes:
    """Connect to the APCUPSd NIS and request its status in raw format.

    :param host: the host which apcupsd is listening on.
    :param port: the port which apcupsd is listening on.
    :return: a bytes object containing raw status obtained from apcupsd.
    """

    reader, writer = await asyncio.open_connection(host, port)
    try:
        writer.write(_STATUS_CMD)
        await writer.drain()

        buffer = await reader.readuntil(_EOF)
        return buffer
    finally:
        writer.close()
        await writer.wait_closed()


def split_unit(value: str) -> tuple[str, str | None]:
    """Split the unit suffix from the value (if available).

    For the set of supported unit suffixes, see aioapcaccess.UNITS.

    :param value: the retrieved value string.
    :return: a tuple consisting of the value and the unit (None if not found).
    """
    for unit in UNITS:
        if not value.endswith(unit):
            continue
        return value[: -len(unit)].strip(), unit

    return value, None
