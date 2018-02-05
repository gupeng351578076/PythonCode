__author__ = 'mocy'
#coding:UTF-8
import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china')
print(res)
res.encoding='utf-8'
# print(res.text)

html_sample='<html><body><h1 id="title">Hello World</h1></body></html>'
soup = BeautifulSoup(html_sample,'html.parser')
print(soup.text)
alink = soup.select('h1')
print(alink)
print(alink[0].text)