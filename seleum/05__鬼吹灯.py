
import os
import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup
import requests


def get_page_source(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def parse_page_source(source):
    book_list = []
    soup = BeautifulSoup(source, 'html.parser')
    a_list = soup.find_all('div', attrs={'class': 'mulu-list-2'})
    for a in a_list:
        a_list = a.find_all('a')
        for href in a_list:
            book_list.append(href['href'])
    return book_list


def get_book_name(book_page):
    book_number = book_page.split('/')[-1].split('.')[0]
    book_chapter_name = book_page.split('/')[-2]
    return book_number, book_chapter_name


async def aio_downlone_one(href, semphore):
    number, c_name = get_book_name(href)
    for c in range(10):
        try:
            async with semphore:
                async with aiohttp.ClientSession() as session:
                    async with session.get(href) as response:
                        source = await response.text()
                        soup = BeautifulSoup(source, 'html.parser')
                        chapter_name = soup.find(
                            'div', attrs={'class': 'content book-content'}).find('h1').text
                        p_content = soup.find(
                            'div', attrs={'class': 'neirong'}).find_all('p')
                        content = [p.text for p in p_content]
                        chapter_content = '\n'.join(content)
                        if not os.path.exists(f'{book_name}/{c_name}'):
                            os.mkdir(f'{book_name}/{c_name}')

                        path = os.path.join(
                            '斗罗大陆', c_name, chapter_name + '.txt')
                        async with aiofiles.open(path, mode='w') as f:
                            await f.write(chapter_content)
                        print(f'{chapter_name}下载完成')
                        return ''
        except Exception as e:
            print(e)
            print(f'{number}.{c_name}下载失败，正在重试第{c}次')
    return href


async def aio_download(href_list):
    print(22222222222,href_list)
    tasks = []
    semphore = asyncio.Semaphore(10)
    for href in href_list:
        tasks.append(asyncio.create_task(aio_downlone_one(href, semphore)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    url = 'https://www.51shucheng.net/wangluo/douluodalu'
    book_name = '斗罗大陆'
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    source = get_page_source(url)
    href_list = parse_page_source(source)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aio_download(href_list))
    loop.close()
