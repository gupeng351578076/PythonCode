__author__ = 'mocy'
#coding:UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import io
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#驱动声明
driver = webdriver.Chrome()
driver.get('http://www.python.org')
assert "Python" in driver.title#断言结果为假出现异常
# print(driver.find_element_by_id("start-shell"))
elem = driver.find_element_by_name("q")
elem.send_keys('pysider')
elem.send_keys(Keys.RETURN)
print(driver.page_source)
