__author__ = 'mocy'
#coding:UTF-8
import  requests
resp = requests.get(url='http://www.baidu.com')
print(type(resp))
print(resp.status_code)
print(resp.cookies)
print(resp.encoding)
resp.encoding = 'utf-8'
print(resp.text)
print(resp.content)