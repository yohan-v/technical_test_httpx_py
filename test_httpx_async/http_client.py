"""HTTP client implementation."""

import httpx
from httpx import ConnectError


class HttpClient:
    """HTTP client implementation."""

    def __init__(self, retries: int = 2):
        """Initialize the application with required settings."""
        self.retries = retries
        self.client = httpx.AsyncClient()

    async def get(self, url: str, **kwargs):
        """Send a GET request to the specified endpoint."""
        for attempt in range(self.retries):
            try:
                response = await self.client.get(url, **kwargs)
                return response
            except ConnectError as e:
                if attempt == self.retries - 1:
                    raise e

    async def close(self):
        """Close the connection."""
        await self.client.aclose()
