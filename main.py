"""Main module for the application."""

import asyncio

from test_httpx_async.http_client import HttpClient


async def main():
    """Demonstrate the usage of the HttpClient() function."""
    client = HttpClient(retries=2)
    try:
        response = await client.get("https://python.test.me")
        print(response.text)
    finally:
        await client.close()


asyncio.run(main())
