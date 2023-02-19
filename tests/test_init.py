"""Test functions for aioapcaccess."""
import asyncio
from unittest.mock import MagicMock, patch

import pytest

from aioapcaccess import parse_raw_status, request_raw_status, request_status

from . import PARSED_DICT, SAMPLE_STATUS


@pytest.mark.asyncio
async def test_request_status():
    """Test top-level API request_status."""
    with patch(
        "aioapcaccess.request_raw_status", return_value=SAMPLE_STATUS
    ) as mock_request_raw_status:
        assert await request_status("testhost", 4242) == PARSED_DICT
        mock_request_raw_status.assert_called_once_with("testhost", 4242)


@pytest.mark.asyncio
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
    """Test parsing raw status"""
    assert parse_raw_status(SAMPLE_STATUS) == PARSED_DICT


def test_parse_error():
    """Test exception when raw string does not end with EOF."""
    status = bytes(SAMPLE_STATUS)
    if status.endswith(b"\x00\x00"):
        status = status[:-2]

    with pytest.raises(ValueError):
        parse_raw_status(status)
