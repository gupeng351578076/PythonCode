__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import requests
from bs4 import BeautifulSoup
import sys
import io
import os

# #获取页面并下载
def GetPageAndDownload(url,filename):
    resp = urllib.request.urlopen(url).read()
    #改变工作目录
    workbefore = os.getcwd()+"\\article"
    os.chdir(workbefore)
    with open(filename.replace('/','_')+".html","wb") as f:
        f.write(resp)
        f.close()
    #改变工作目录回去
    workafter = os.getcwd()[:-8]
    os.chdir(workafter)

#获取二级网页
def twoPage(url):
    resp1 = requests.get(url)
    resp1.encoding='utf-8'
    soup = BeautifulSoup(resp1.text,'html.parser')
    # 获取二级列表
    listtitle= []
    listhref = []
    listall = []
    for i in soup.select('.article-content p a'):
        try:
            if i['title']!="":
                listtitle.append(i['title'])
                listhref.append(i['href'])
        except KeyError as e:
            print(e)
        listall.append(listtitle)
        listall.append(listhref)
    return listall

#主函数
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url = 'https://cuiqingcai.com/1052.html'#首页url
GetPageAndDownload(url,'index')#获取首页并下载
list = twoPage(url)#获取二级页面并下载
for i,href in enumerate(list[1]):
    GetPageAndDownload(href,list[0][i])
