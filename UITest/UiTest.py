# coding=utf-8
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.maximize_window()
# browser.set_window_size(1920,1000)

driver.get('http://www.baidu.com')

try:
    # browser.back()
    # browser.forward()
    # Chrome.find_element(By.ID, 'kw').send_keys('今天的热点')
    # Chrome.find_element(By.ID, 'su').send_keys(Keys.ENTER)
    print(driver.find_element(By.ID, 'su').size)  # 返回尺寸大小
    print(driver.find_element(By.PARTIAL_LINK_TEXT, '使用百度').text)  # 返回元素的文本
    print(driver.find_element(By.ID, 'su').get_attribute('value'))


except selenium.common.exceptions.NoSuchElementException as e:
    print("元素有异常：", e.msg)

except:
    print("未知异常！")

finally:
    time.sleep(5)
    print('即将关闭浏览器！')
    driver.quit()
