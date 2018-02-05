__author__ = 'mocy'
#coding:UTF-8
import requests
import json
import re

from bs4 import BeautifulSoup
# from datetime import datetime
# import io
# import sys
# #改变python3默认输出编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#以上作为基本引用

#获取评论数量
def getCommentCounts(newsurl):
    newsid = re.search('doc-i(.*).shtml',newsurl).group(1)
    commentURL='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    comments = requests.get(commentURL.format(newsid))
    com_num = json.loads(comments.text.strip('var data='))['result']['count']['total']
    return com_num

#获取新闻详情页
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('.main-title')[0].text
    result['time'] = soup.select('.date-source')[0].contents[0]
    result['article'] = ' '.join([p.text.strip() for p in soup.select('.article p')[:-1]])
    result['editor'] = soup.select('.show_author')[0].text.lstrip('责任编辑：')
    result['com_num'] = getCommentCounts(newsurl)
    return result

#获取新闻列表
def getNewsList(sortURL):
    res = requests.get(sortURL)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    for news in soup.select('.news-item'):
        if( len(news.select('h2')) >0 ):
            h2 = news.select('h2')[0].text
            time = news.select('.time')[0].text
            newsurl = news.select('a')[0]['href']
            print(time,h2,newsurl)
            # wenzhang = getNewsDetail(newsurl)
            # print(time,h2,newsurl,wenzhang)

#MAIN-获取新闻
getNewsList('http://news.sina.com.cn/china/')
# print(getNewsDetail('http://news.sina.com.cn/c/2017-09-05/doc-ifykpzey4568845.shtml'))