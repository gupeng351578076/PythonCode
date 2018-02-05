__author__ = 'mocy'
#coding:UTF-8
import re
# #1匹配任意数字
# #match和search的区别是前者只会匹配开始位置，后者扫描整个字符串进行查找
# pattern = re.compile(r'\d{1}')
# result = re.search(pattern,'a123456')
# print(result.group())

# #2分割字符串根据匹配到的数字
# pattern = re.compile(r'\d+')
# result = re.split(pattern,'a1b2c3d')
# print(result)

# #3搜索字符串，以列表形式展示匹配的结果
# pattern = re.compile(r'\d+')
# result = re.findall(pattern,'a1b2c3d456')
# print(result)

# #4搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
# pattern = re.compile(r'\d+')
# for i in re.finditer(pattern,'one1two2three3four4'):
#     print(i.group())

#5使用repl替换string中每一个匹配的子串后返回替换后的字符串。
pattern = re.compile(r'(\w+) (\w+)')
s = 'i say,hello world'
print(re.sub(pattern,r'\2 \1',s))
#另一种写法，直接用匹配规则调用匹配方法
result = pattern.sub(r'\2 \1',s)
print(result)

