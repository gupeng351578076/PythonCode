__author__ = 'mocy'
#coding:UTF-8
import requests
import io
import sys
#改变python3默认输出编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china')
res.encoding='utf-8'
soup = BeautifulSoup(res.text,'html.parser')
#循环出所有新闻模块
for news in soup.select('.news-item'):
    if(len(news.select('h2'))>0):
        h2 = news.select('h2')[0].text#获取新闻标题
        time = news.select('.time')[0].text#获取时间
        a = news.select('a')[0]['href']
        print(h2,time,a)

