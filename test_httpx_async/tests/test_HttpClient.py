"""Implement and test the HTTP client functionality."""

from unittest.mock import AsyncMock, patch

import pytest
from httpx import ConnectError

from test_httpx_async.http_client import HttpClient


@pytest.mark.asyncio
async def test_http_client_retries_on_connect_error():
    """Test if the HTTP client retries requests on a connection error."""
    async_mock = AsyncMock(side_effect=ConnectError("Connection error"))
    retries = 2

    with patch("httpx.AsyncClient.get", async_mock):
        client = HttpClient(retries=retries)

        with pytest.raises(ConnectError):
            await client.get("http://python.test.me")

        assert async_mock.call_count == retries
        await client.close()
