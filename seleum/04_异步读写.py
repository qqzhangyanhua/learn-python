import asyncio
import aiofiles




async def main():
    async with aiofiles.open('01.get.py', ) as f:
        source = await f.readlines()
        print(source)

asyncio.run(main())
