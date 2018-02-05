__author__ = 'mocy'
#coding:UTF-8
import sys
import io
# #改变python3默认输出编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from pyquery import PyQuery as pq
doc = pq('http://www.baidu.com')
print(doc.html())
