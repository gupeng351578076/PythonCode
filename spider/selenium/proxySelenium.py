__author__ = 'mocy'
#coding:UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import io
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://192.168.133.4:80')
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://www.python.org/')
elem = chrome.find_element_by_name("q")
elem.send_keys('pysider')
elem.send_keys(Keys.RETURN)
print(chrome.page_source)
chrome.quit()
