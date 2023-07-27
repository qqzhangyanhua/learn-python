
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import json
import time
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()


driver.get(
    'http://so.gushiwen.cn/user/collect.aspx')

with open('cookie.text', 'r') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    cookie_dict = {}
    for k,v in cookie.items():
        cookie_dict[k] = v
        #添加cookie
    driver.add_cookie(cookie_dict)
driver.refresh()  # 刷新页面
driver.get(
'http://so.gushiwen.cn/user/collect.aspx')


print('登陆成功')
time.sleep(100)
