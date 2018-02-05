__author__ = 'mocy'
#coding:UTF-8
import urllib.request
import io
import sys
# #改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
resp = urllib.request.urlopen('http://www.baidu.com')
print(resp.read().decode('utf-8'))#获取相应体内容
#获取相应信息（状态码  头信息）
print(resp.status,resp.getheaders())

