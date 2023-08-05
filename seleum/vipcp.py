
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import base64
import json
import requests
import time
import random
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()


def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post(
        "http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]


driver.get(
    'https://vipc9.com/')
close_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/button')
close_btn.click()
time.sleep(random.randint(1, 2))


btn = driver.find_element(By.XPATH,'/html/body/div/header/div[1]/div/div[5]/div[2]')
btn.click()
# 准备填入帐号密码
username = driver.find_element(By.XPATH, '//*[@id="login"]/div/form/div[1]/input')
username.send_keys('freddie')
password = driver.find_element(By.XPATH, '//*[@id="login"]/div/form/div[2]/input').send_keys('a123456')
login = driver.find_element(By.XPATH, '//*[@id="login"]/div/form/button')
login.click()

# 获取列表
list = driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/main/div[4]/div/div/div/div/main/div[2]/div/article/div/header/h2/a')
print('list====',list)
for i in list:
    href = i.get_attribute('href')
    title = i.get_attribute('title')
    print('href====',href,'title====',title)

time.sleep(100)
