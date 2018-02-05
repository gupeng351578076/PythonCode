__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import urllib3
import http.cookiejar
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
req = urllib.request.Request('http://www.baidu.com')
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resp = opener.open(req)
print(resp.read())
