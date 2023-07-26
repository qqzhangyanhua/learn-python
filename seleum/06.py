
from selenium.webdriver import Chrome
from selenium import webdriver
import time
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()

driver.get('https://www.haizol.com/')
time.sleep(103)
