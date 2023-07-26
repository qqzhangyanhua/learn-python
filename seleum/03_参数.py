import aiohttp
import asyncio


async def fetch(session, url):
    params={'name':"2222"}
    async with session.get(url,params=params) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, 'http://httpbin.org/get')
        print(source)

asyncio.run(main())
