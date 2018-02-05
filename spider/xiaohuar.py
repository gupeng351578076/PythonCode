__author__ = 'mocy'
#coding:UTF-8
#http://www.xiaohuar.com
import requests
from bs4 import BeautifulSoup
import io
import sys
import urllib.request
import time
import os
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

#获取小花儿函数(小花儿的姓名学校照片好评数量)
def getGirs(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    res = requests.get(url,headers=header,timeout=10)
    res.encoding ='gb2312'
    soup = BeautifulSoup(res.text,'html.parser')
    #获取图片地址列表
    listimg = []
    for img in soup.select('.twoline')[0].select('img'):
        listimg.append(img['lazysrc'])
    #获取姓名列表
    listname = []
    for name in soup.select('.twoline')[0].select('span'):
        listname.append(name.text)
    #获取学校名称
    listschool = []
    for school in soup.select('.twoline')[0].select('.b1'):
        listschool.append(school.text)
    #获取好评数
    listgood = []
    for good in soup.select('.twoline')[0].select('.b2'):
        listgood.append(good.text)
    listall = []
    listall.append(listname)
    listall.append(listschool)
    listall.append(listimg)
    listall.append(listgood)
    return listall

#截取最后出现该字符的位置
def find_last(string,str):
    lastposition = -1
    while True:
        position = string.find(str,lastposition+1)
        if position==-1:
            return lastposition
        lastposition = position

#定义下载小花儿图片的函数
def downloadImg(url):
    resp = urllib.request.urlopen(url)
    html = resp.read()
    #截取后缀名
    lastpositon = find_last(url,'.')
    hzname = url[lastpositon+1:]
    #拼接完整文件名
    file_name = str(int(time.time()*10000000//1000))+'.'+hzname
    #改变当前工作目录
    workbefore = os.getcwd()+"\\xhpic"
    os.chdir(workbefore)
    #写图片
    temp_file = open(file_name, 'wb')
    temp_file.write(html)
    temp_file.close()
    #改变工作目录回去
    workafter = os.getcwd()[:-6]
    os.chdir(workafter)

# getGirs('http://www.xiaohuar.com')
# downloadImg('http://www.xiaohuar.com/d/file/20150123013303170.jpg')
# worknow = os.getcwd()+"\\xhpic"
# print(worknow)

#创建文件夹
#获取小花儿信息
listall = getGirs('http://www.xiaohuar.com')
#写入数据库
#循环下载小花儿照片
for img in listall[2]:
    # print(type(str(img)))
    try:
        if img.find('http://')==-1:
            url = 'http://www.xiaohuar.com'+img
            downloadImg(url)
        else:
            downloadImg(img)
    except:
        print('有问题')
