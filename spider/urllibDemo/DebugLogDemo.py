__author__ = 'mocy'
#coding:UTF-8
import urllib.request
http_handler = urllib.request.HTTPHandler(debuglevel=1)
https_handler = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(http_handler,https_handler)
urllib.request.install_opener(opener)
resp = urllib.request.urlopen('http://www.baidu.com')