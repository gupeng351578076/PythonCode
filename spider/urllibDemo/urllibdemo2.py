__author__ = 'mocy'
#coding:UTF-8
# import urllib.request
# resp = urllib.request.urlopen('https://python.org')
# print(resp.read().decode('utf-8'))
from urllib import request, parse
import urllib.request
url = 'https://www.python.org'
dict = {
    'name': 'pengpeng'
}
#请求数据
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, method='GET')
#添加请求头
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
#代理设置
proxy_handler = urllib.request.ProxyHandler({
    'http':'http://198.168.133.4:80'
})
opener = urllib.request.build_opener(proxy_handler)
#访问获取相应
resp = opener.open(req)
print(resp.read().decode('utf-8'))