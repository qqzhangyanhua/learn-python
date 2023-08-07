
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import base64
import json
import requests
import time
import random
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()



driver.get(
    'https://vipc9.com/')
close_btn = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/button')
close_btn.click()
time.sleep(random.randint(1, 2))


btn = driver.find_element(
    By.XPATH, '/html/body/div/header/div[1]/div/div[5]/div[2]')
btn.click()
# 准备填入帐号密码
username = driver.find_element(
    By.XPATH, '//*[@id="login"]/div/form/div[1]/input')
username.send_keys('freddie')
password = driver.find_element(
    By.XPATH, '//*[@id="login"]/div/form/div[2]/input').send_keys('a123456')
login = driver.find_element(By.XPATH, '//*[@id="login"]/div/form/button')
login.click()

cookies = driver.get_cookies()
jsonCookie = json.dumps(cookies)
with open('vip_cookie.text', 'w') as f:
    f.write(jsonCookie)
print('登陆成功')
time.sleep(100)

# def go_detail(val):
#     print('detail======',val)
# # 获取列表
# list = driver.find_elements(
#     By.XPATH, '/html/body/div[1]/div[2]/div/main/div[4]/div/div/div/div/main/div[2]/div/article/div/header/h2/a')
# print('list====', list)
# for i in list:
#     try:
#         href = i.get_attribute('href')
#         title = i.get_attribute('title')
#         time.sleep(random.random()+0.5)
#         i.click()
#         print('href====', href, 'title====', title)
#     except Exception as e:
#         print(e)

# time.sleep(100)
