import requests
import os
import time
import random
from bs4 import BeautifulSoup
main_url ='https://www.shicimingju.com/bookmark/sidamingzhu.html'
headers = {
     'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
response = requests.get(main_url, headers=headers)
response.encoding = 'utf-8'
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
# 取出四大名著的链接