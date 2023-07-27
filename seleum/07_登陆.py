
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
    'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
username = driver.find_element(By.XPATH, '//*[@id="email"]')
username.send_keys('13251953746')
password = driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('a123456')
viw_code = driver.find_element(By.XPATH, '//*[@id="imgCode"]')
viw_code.screenshot('code.png')
img_path = "./code.png"
result = base64_api(uname='13251953746', pwd='a123456',
                    img=img_path, typeid=3)
print('code==',result)
code = driver.find_element(By.XPATH, '//*[@id="code"]').send_keys(result)
login = driver.find_element(By.XPATH, '//*[@id="denglu"]')
login.click()

# 处理cookie

cookies = driver.get_cookies()
jsonCookie = json.dumps(cookies)
with open('cookie.text', 'w') as f:
    f.write(jsonCookie)
print('登陆成功')
time.sleep(100)
