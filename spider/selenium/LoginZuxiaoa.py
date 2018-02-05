__author__ = 'mocy'
#coding:UTF-8
import sys
import io
import os
import urllib.request
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#初始化配置
def initWork():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

#验证码获取
def getValidate():
    img_url = 'http://passport.cqzuxia.com/account/LoadValidCode'
    img_data = urllib.request.urlopen(img_url).read()
    #改变当前工作目录
    workbefore = os.getcwd()+"\\ValidateImage"
    os.chdir(workbefore)
    #写图片
    temp_file = open('validate.png', 'wb')
    temp_file.write(img_data)
    temp_file.close()
    #改变工作目录回去
    workafter = os.getcwd()[:-14]
    os.chdir(workafter)


#执行登陆
def handleLogin(driver,url):
    username = 'gp2015'
    password = 'gp2015'
    driver.get(url)
    cookies = driver.get_cookies()
    #获取账号登陆页面
    try:
        #不用模拟账号登陆链接，表单实际上是隐藏起来的
        #填充用户名和密码和验证码
        js1='document.getElementById("username-login").style.display="block";'
        js2='document.getElementById("username-login").style.opacity="1.0";'
        js3='document.getElementById("qr-login").style.display="none";'
        js4='document.getElementById("qr-login").style.opacity="0";'
        driver.execute_script(js3)
        driver.execute_script(js4)
        driver.execute_script(js1)
        driver.execute_script(js2)
        elem1 = driver.find_element_by_css_selector("#username")
        elem2 = driver.find_element_by_css_selector("#password")
        elem3 = driver.find_element_by_css_selector("#ValidCode")
        elem = driver.find_element_by_class_name("btn-primary")
        elem1.send_keys(username)
        elem2.send_keys(password)
        #获取验证码输入
        elem3.send_keys('233F')
        #添加cookie
        # driver.add_cookie(cookies)
        elem.send_keys(Keys.ENTER)
    except NoSuchElementException as e:
        print(e)
    # finally:
        # driver.quit()


#主函数
if __name__ =='__main__':
    driver = initWork()
    url = 'http://passport.cqzuxia.com/account/login?ReturnUrl=http%3a%2f%2ferp.cqzuxia.com%2f'
    handleLogin(driver,url)