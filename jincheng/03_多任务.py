import asyncio
import time


async def func1(url):
    print('开始执行', url)
    return url


def func2(f):
    print('返回值===', f.result())


async def main():
    url_list = ['task1', 'task2', 'task3']
    tasks = []
    for url in url_list:
        con = func1(url)
        task = asyncio.ensure_future(con)
        task.add_done_callback(func2)
        tasks.append(task)
    await asyncio.wait(tasks)
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('end')
