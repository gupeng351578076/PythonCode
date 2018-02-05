__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import re
import sys
import io

def getPage(page,url):
    try:
        #请求头信息
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        request = urllib.request.Request(url,headers=headers)
        #代理设置
        proxy_handler = urllib.request.ProxyHandler({
            'http':'http://198.168.133.4:80'
        })
        opener = urllib.request.build_opener(proxy_handler)
        #访问获取相应
        response = opener.open(request)
        # response = urllib.request.urlopen(request)
        return response.read()
    except  urllib.request.URLError as e:
        if hasattr(e,"code"):
            print (e.code)
        if hasattr(e,'reason'):
            print(e.reason)

#匹配 发布内容 发布人  点赞数
def getDuanzi(content):
    list = []
    pattern1 = re.compile('<div class="content">.*?<span>(.*?)</span>.*?',re.S)
    items1 = pattern1.findall(content)
    list.append(items1)
    pattern2 = re.compile('<div class="author clearfix".*?<h2>(.*?)</h2>',re.S)
    items2 = pattern2.findall(content)
    list.append(items2)
    pattern3 = re.compile('<div class="stats">.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>',re.S)
    items3 = pattern3.findall(content)
    list.append(items3)
    return list

#拿到热门总页数
def getHotPageNumber(page,url):
    content = getPage(page,url)
    pattern = re.compile('<span class="page-numbers">(.*?)</span>',re.S)
    pagenumber = pattern.findall(content.decode('utf-8'))
    # pagenumber[:-1]
    return (pagenumber[-1].replace("\n","")).strip()+''

#主函数测试
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
page = 1
url = 'https://www.qiushibaike.com/hot/page/'+str(page)
#获取页数
pagenumber = getHotPageNumber(page,url)
#循环获取每一页的东西,匹配 存入文本
for i in range(int(int(pagenumber))):
    page = i+1
    content = getPage(page,url)
    list = getDuanzi(content.decode('utf-8'))
    file = open('qsbkdata.txt','a+')
    file.write(str(list))
    file.close()