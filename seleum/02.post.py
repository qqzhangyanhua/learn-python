import aiohttp
import asyncio


async def fetch(session, url):
    async with session.post(url,data={'name':"2222"}) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, 'http://httpbin.org/post')
        print(source)

asyncio.run(main())
