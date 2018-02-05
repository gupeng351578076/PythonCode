__author__ = 'mocy'
#coding:UTF-8
import requests
import sys
import io
# #改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
proxies = {
    'http':'http://192.168.133.4:80',
    'http':'http://127.0.0.1:80'
}
try:
    response = requests.get('https://www.csdn.net/',proxies = proxies)
    response.encoding = 'utf-8'
    print(response.text)
except BaseException as e:
    print(e)