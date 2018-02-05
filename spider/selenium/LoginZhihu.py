__author__ = 'mocy'
#coding:UTF-8
import sys
import io
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#初始化浏览器模拟操作
def initWork():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

#执行登陆
def login(username,password,driver,url):
    driver.get(url)
    cookies = driver.get_cookies()
    try:
        #变换成登陆页面
        elemr = driver.find_element_by_css_selector(".SignContainer-switch").find_element_by_tag_name('span')
        elemr.click()
        elemu = driver.find_element_by_name("username")
        elemp = driver.find_element_by_name("password")
        sleep(3)
        elemu.send_keys(username)
        sleep(3)
        elemp.send_keys(password)
        sleep(3)
        # driver.add_cookie(cookies)
        elem = driver.find_element_by_css_selector(".SignFlow-submitButton")
        print(elem.text)
        elem.send_keys(Keys.ENTER)
    except NoSuchElementException as e:
        print(e)

#主函数
if __name__ =='__main__':
    driver = initWork()
    url = 'https://www.zhihu.com/signup?next=%2F'
    login('15184376753','******',driver,url)