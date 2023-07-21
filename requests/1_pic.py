import requests
import os
import time
import random
from lxml import etree
from urllib import request as req

url = 'http://pic.netbian.com/'

headers = {
     'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
response = requests.get(url, headers=headers)
response.encoding = 'gbk'
# print(response.text)
html = etree.HTML(response.text)
scop = html.xpath('//ul[@class="clearfix"]/li')
# print(scop)  
for i in scop:
    # print(i)
    img = i.xpath('./a/span/img/@src')
    img_url = 'http://pic.netbian.com' + img[0]
    img_name =i.xpath('./a/b/text()')
    path = './img'
    if not os.path.exists(path):
        os.mkdir(path)
    req.urlretrieve(img_url, os.path.join(path, img_name[0]+'.jpg'))
    time.sleep(random.randint(1, 3))
    # print(img)
    #