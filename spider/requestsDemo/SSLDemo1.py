__author__ = 'mocy'
#coding:UTF-8
import requests
import sys
import io
#改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
url = 'https://kyfw.12306.cn/otn/'
resp = requests.get(url,verify=True)
resp.encoding='utf-8'
print(resp.text)