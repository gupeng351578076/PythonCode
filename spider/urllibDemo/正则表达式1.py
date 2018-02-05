__author__ = 'mocy'
#coding:UTF-8
import re
#匹配模式
pattern = re.compile(r'hello')
result1 = re.match(pattern,'hel')
result2 = re.match(pattern,'hello pengpeng')
print(result1)#匹配不成功返回None
if result1:
    print(result2.group())#匹配成功返回分组信息
else:
    print('匹配失败')
if result2:
    print(result2.group())#匹配成功返回分组信息
else:
    print('匹配失败')
#正则表达式规则见文件夹中正则表达式规则.PNG