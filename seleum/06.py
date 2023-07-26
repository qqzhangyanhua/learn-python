
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import time
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()

driver.get('https://www.gushiwen.cn/')
txtKey =driver.find_element(By.ID,'txtKey')
txtKey.send_keys('李白')
time.sleep(100)
