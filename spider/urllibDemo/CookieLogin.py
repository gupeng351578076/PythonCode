__author__ = 'mocy'
#coding:utf-8
import urllib
# import urllib.request
import http.cookiejar
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
values = {}
values['userName'] = "351578076@qq.com"
values['password'] = "******"
postdata = urllib.parse.urlencode(values).encode(encoding='UTF-8')
loginUrl = 'https://passport.baidu.com/v2/?login'
result = opener.open(loginUrl,postdata)
print(type(result))
print('--------------------------------------------------')
cookie.save(ignore_discard=True,ignore_expires=True)
otherUrl = 'https://passport.baidu.com/center?_t=1516854199'
result = opener.open(otherUrl)
print(result.read().decode('utf-8'))

