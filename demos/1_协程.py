

import asyncio
import  aiohttp
from lxml import etree
async def down_load_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            page_source = await resp.text() #获取网页源码
            html = etree.HTML(page_source)
            #获取所有的小说的url
            print(html.xpath('/html/body/div[4]/div[3]/div[2]/table/tbody/tr[2]/td[2]/a/@href'))
            print('-------------------')
    
async def main():
    tasks = []
    for i in range(1,6):
        url = f'https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{i}.html'
        #每一个url都创建一个协程
        task = asyncio.create_task(down_load_one(url))
        tasks.append(task)
    #等待所有的协程执行完毕
    await asyncio.wait(tasks)

if __name__ == '__main__':
    # asyncio.run(main())
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())

