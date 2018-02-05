__author__ = 'mocy'
#coding:UTF-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime
res = requests.get('http://news.sina.com.cn/c/2017-09-05/doc-ifykpzey4568845.shtml')
res.encoding='utf-8'
soup = BeautifulSoup(res.text,'html.parser')
#抓取标题
title = soup.select('#artibodyTitle')[0].text
print(title)
#时间
newstime = soup.select('#navtimeSource')[0].contents[0].strip()
print(newstime)
#格式化日期
time = datetime.strptime(newstime,'%Y年%m月%d日%H:%M')
print(time)
#文章来源
hq = soup.select('.time-source span')[0].text
print(hq)
#正文
#article = soup.select('#artibody p')[:-1]
#print(article)
#列表拆分合并字符串
article = []
for p in soup.select('#artibody p')[:-1]:
    article.append(p.text.strip())
articles = ''.join(article)#列表转换成字符串
print(articles)
