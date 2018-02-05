__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import http.cookiejar
cookie = http.cookiejar.MozillaCookieJar(filename='cookie.txt')
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resp = opener.open('http://www.baidu.com')
#ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
# ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
cookie.save(ignore_discard=True,ignore_expires=True)