__author__ = 'mocy'
#coding:UTF-8
from lxml import etree
import sys
import io
#改变python3默认输出编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
html = etree.parse('hello.html')
result = etree.tostring(html,pretty_print=True)
print(result)

#获取li标签
resultli = html.xpath('//li')
print(len(resultli))
print(resultli[0])

#获取li标签的class
resultc = html.xpath('//li/@class')
print(resultc)

#获取href为link1.html的a标签
resulthref = html.xpath('//li/a[@href="link1.html"]')
print(resulthref)

#获取li下的span
resultspan = html.xpath('//li//span')
print(resultspan)

#获取li下的class不包括自身
result1 = html.xpath('//li/a//@class')
print(result1)

#获取最后一个li的a的href
result2= html.xpath('//li[last()]/a/@href')
print(result2)

#获取倒数第二个元素内容
result3 = html.xpath('//li[last()-1]/a')
print(result3[0].text)

#获取class为s的标签名
result4 = html.xpath('//*[@class="s"]')
print(result4[0].tag)
