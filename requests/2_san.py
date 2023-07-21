import requests
from lxml import etree
import time
import random
headers = {
     'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
etree_html = etree.HTML(response.text)

title_list = etree_html.xpath('//*[@id="main_left"]/div/div[4]/ul/li/a/text()')
href_list = etree_html.xpath('//*[@id="main_left"]/div/div[4]/ul/li/a/@href')

for i in range(len(title_list)):
    url = 'https://www.shicimingju.com' + href_list[i]
    # print(title_list[i], url)
    req = requests.get(url, headers=headers)
    req.encoding = 'utf-8'
    tree = etree.HTML(req.text)
    content = tree.xpath('//*[@id="main_left"]/div[1]/div/p/text()')
    time.sleep(random.randint(1, 3))
    # print(content)
    with open('三国演义.txt', 'a', encoding='utf-8') as f:
        f.write(title_list[i] + '\n')
        for j in content:
            f.write(j + '\n')
        f.write('\n')
    print(title_list[i], '写入成功')
    print('------------------')
    # break
