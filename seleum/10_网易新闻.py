from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import random
Chrome.driver = '/path/to/chromedriver'
driver = Chrome()
driver.get('https://news.163.com/')


def window_top_to(stop_length):
    # 处理滚动条

    step_length = 800  # 每次滑动的距离
    top = 0
    while True:
        if stop_length:
            if stop_length - step_length < 0:
                driver.execute_script(
                    'window.scrollBy(0, {})'.format(step_length))
                break

        stop_length -= step_length
        # 开始滚动
        driver.execute_script('window.scrollBy(0, {})'.format(step_length))
        # 随机停止时间
        time.sleep(random.random()+0.5)
        # 获取当前滚动条的位置
        check_height = driver.execute_script(
            'return document.documentElement.scrollTop')
        if check_height == top:
            break
        top = check_height
    print('不要滑动了')


for i in range(1, 4):
    try:
        window_top_to(24455)
        # 走到这里证明改点击了
        more = driver.find_element(
            By.XPATH, '//*[@id="index2016_wrap"]/div[3]/div[2]/div[3]/div[2]/div[5]/div/a[3]')
        # more.click()
        driver.execute_script('arguments[0].click();', more)
        time.sleep(random.random()+0.5)
        print(f'第{i}次加载更多了')
    except Exception as e:
        print('加载更多了 ')
        break

time.sleep(125)
