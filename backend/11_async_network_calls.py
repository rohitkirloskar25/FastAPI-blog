import time
import asyncio
import aiohttp

async def make_request(session, req_n):
    url = "https://httpbin.org/get"
    print(f"making request {req_n}")
    async with session.get(url) as resp:
        if resp.status_code == 200:
            await resp.text()

async def main():
      request_count = 10
      async with aiohttp.ClientSession() as session:
            await asyncio.gather(
                  *[make_request(session, i) for i in range(request_count)]
            )

loop = asyncio.get_event_loop()