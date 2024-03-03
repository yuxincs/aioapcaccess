"""Test functions for aioapcaccess."""

import asyncio
from unittest.mock import MagicMock, patch

import pytest
from aioapcaccess import parse_raw_status, request_raw_status, request_status, split_unit

from . import PARSED_DICT, SAMPLE_STATUS


async def test_request_status():
    """Test top-level API request_status."""
    with patch(
        "aioapcaccess.request_raw_status", return_value=SAMPLE_STATUS
    ) as mock_request_raw_status:
        assert await request_status("testhost", 4242) == PARSED_DICT
        mock_request_raw_status.assert_called_once_with("testhost", 4242)


async def test_request_raw_status():
    """Test requesting raw status from apcupsd NIC."""
    with patch("asyncio.open_connection") as mock_open_connection:
        mock_reader = asyncio.StreamReader()
        mock_reader.feed_data(SAMPLE_STATUS)

        mock_writer = MagicMock(spec=asyncio.StreamWriter)
        mock_open_connection.return_value = (mock_reader, mock_writer)

        result = await request_raw_status("testhost", 4242)
        assert result == SAMPLE_STATUS


def test_parse_raw_status():
    """Test parsing raw status."""
    assert parse_raw_status(SAMPLE_STATUS) == PARSED_DICT


def test_parse_error():
    """Test exception when raw string does not end with EOF."""
    status = bytes(SAMPLE_STATUS)
    if status.endswith(b"\x00\x00"):
        status = status[:-2]

    with pytest.raises(ValueError):
        parse_raw_status(status)


@pytest.mark.parametrize(
    "raw_value,value,unit",
    [
        ("15.0 Percent", "15.0", "Percent"),
        ("16.0 Unrecognized Unit", "16.0 Unrecognized Unit", None),
        ("18.0 Percent Load Capacity", "18.0", "Percent Load Capacity"),
        ("32.0 C Internal", "32.0", "C Internal"),
        ("7 days", "7", "days"),
    ],
)
def test_split_unit(raw_value: str, value: str, unit: str):
    v, u = split_unit(raw_value)
    assert v == value
    assert u == unit
