# coding=utf-8
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')

try:
    """浏览器操作"""
    driver.maximize_window()
    driver.set_window_size(1920, 1000)
    driver.back()
    driver.forward()

    """元素的简单操作"""
    driver.find_element(By.ID, 'kw').send_keys('今天的热点')
    driver.find_element(By.ID, 'su').click()
    driver.find_element(By.ID, 'kw').clear()

    """返回元素的属性"""
    print(driver.find_element(By.ID, 'su').size)  # 返回尺寸大小
    print(driver.find_element(By.PARTIAL_LINK_TEXT, '使用百度').text)  # 返回元素的文本
    print(driver.find_element(By.ID, 'su').get_attribute('value'))  # 返回元素的属性值
    print(driver.find_element(By.ID, 'su').is_displayed())  # 返回元素结果是否用户可见

    """鼠标的操作事件"""
    MouseElement = driver.find_element(By.ID, 'su')
    ActionChains(driver).context_click(MouseElement).perform()  # 右击
    ActionChains(driver).double_click(MouseElement).perform()  # 双击击
    ActionChains(driver).drag_and_drop(MouseElement, MouseElement).perform()  # 拖动
    ActionChains(driver).move_to_element(MouseElement).perform()  # 鼠标悬停在一个元素上
    ActionChains(driver).click_and_hold(MouseElement).perform()  # 按下鼠标左键在一个元素上

    """键盘事件"""
    driver.find_element(By.ID, 'su').send_keys(Keys.ENTER)
    driver.find_element(By.ID, 'su').send_keys(Keys.BACK_SPACE)
    driver.find_element(By.ID, 'su').send_keys(Keys.DELETE)
    driver.find_element(By.ID, 'su').send_keys(Keys.CONTROL, 'a')

    """打印信息"""
    print(driver.title)
    print(driver.current_url)

    """设置等待时间"""
    time.sleep(2)
    driver.implicitly_wait(30)  # 在一定时间范围内智能的等待

    """
    WebDriverWait的使用：
    WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    driver - WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
    timeout - 最长超时时间，默认以秒为单位
    poll_frequency - 休眠时间的间隔（步长）时间，默认为 0.5 秒
    ignored_exceptions - 超时后的异常信息，默认情况下抛 NoSuchElementException 异常
    !---
    WebDriverWai()一般由 unit()或 until_not()方法配合使用:
    until(method, message='')：调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
    until_not(method, message='')：调用该方法提供的驱动程序作为一个参数，直到返回值为 False。
    """
    WebDriverWait(driver=driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None).until(lambda driver: driver.find_element(By.ID, 'kw'))

    """元素组"""
    elements = driver.find_elements(By.TAG_NAME, '')
    for element in elements:
        element.click()


except selenium.common.exceptions.NoSuchElementException as e:
    print("元素有异常：", e.msg)

except:
    print("未知异常！")

finally:
    time.sleep(5)
    print('即将关闭浏览器！')
    driver.quit()
