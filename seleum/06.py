
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

import time
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()

driver.get('https://www.gushiwen.cn/')
txtKey =driver.find_element(By.XPATH,'//*[@id="txtKey"]')
txtKey.send_keys('唐诗')
btnSearch = driver.find_element(By.XPATH,'//*[@id="search"]/form/input[3]')
btnSearch.click()
time.sleep(100)
