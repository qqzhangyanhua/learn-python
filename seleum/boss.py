
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import base64
import json
import requests
import time
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()
driver.get('https://www.lagou.com/')

driver.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[2]/a').click()
driver.find_element(
    By.XPATH, '//*[@id="search_input"]').send_keys('前端', Keys.ENTER)
time.sleep(2)
list = driver.find_elements(By.XPATH, '//*[@id="openWinPostion"]')
num = 0
print(list.__len__())
while num < 15:
    list[num].click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    job_detail = driver.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
    print(job_detail)
    num += 1

time.sleep(100)
