import requests
import os
import time
import random
from bs4 import BeautifulSoup


def get_html(main_url):
    headers = {
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(main_url, headers=headers)
    response.encoding = 'utf-8'
    # print(response.text)
    return BeautifulSoup(response.text, 'lxml')


def get_book(soup):
    # 取出四大名著的链接
    div = soup.find_all('div', class_="book-item")
    dic = {}
    # print(div)
    base_url = 'https://www.shicimingju.com'
    for con in div:
        # 获取书的名字
        book_name = con.get_text().replace('\n', '').replace(' ', '')
        # 获取书的链接
        book_url = con.a['href']
        # 保存到字典中
        dic[book_name] = base_url + book_url
    return dic


def get_book_mulu(soup):
    # 取出四大名著的链接
    div = soup.find_all('div', class_="book-mulu")
    mulu_dic = {}
    for d in div:
        # 抓去超链接
        mulu_href = d.find_all('a')
        for m in mulu_href:
            # 获取章节标题
            title = m.get_text()
            # 获取章节链接
            href = m['href']
            # 拼接章节链接
            url = 'https://www.shicimingju.com' + href
            # 保存到字典中
            mulu_dic[title] = url
    return mulu_dic

# 获取章节内容


def get_book_content(title, content):
    con_dic = {}
    div = content.find('div', class_="chapter_content")
    # 获取章节内容
    text = div.text
    # 保存到字典中
    con_dic[title] = text
    return con_dic


def save_book(book_name, book_val):
    # 判断文件夹是否存在
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    # 判断文件是否存在
    for title in book_val:
        path = os.path.join(book_name, title + '.txt')
        with open(path, 'a') as f:
            f.write(book_val[title])
            print(f'{book_name}==={title} 下载完成', end='\n')


def main(main_url):
    soup = get_html(main_url)
    book_dic = get_book(soup)
    for con in book_dic:
        html = get_html(book_dic[con])
        mulu_dic = get_book_mulu(html)
        for title, url in mulu_dic.items():
          #   print(title, url)
            # 获取章节内容
            content = get_html(url)
            book_val = get_book_content(title, content)
            # 保存到文件中
            save_book(con, book_val)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    main_url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    main(main_url)
