__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import http.cookiejar
# CookieJar对象保存cookie
cookie = http.cookiejar.CookieJar()
# cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(handler)
resp = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name='+item.name)
    print('Value='+item.value)