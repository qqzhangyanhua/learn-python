
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import base64
import json
import requests
import time
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
    'https://passport.haizol.com/pst/login')
username = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/form/div[1]/div/div/input')
username.send_keys('15162606973')
password = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/form/div[2]/div/div/input').send_keys('a12345678')

login = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div/div/form/div[4]/div/button')
login.click()
time.sleep(100)
