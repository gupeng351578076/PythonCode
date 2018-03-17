__author__ = 'mocy'
#coding:UTF-8
#针对字典的迭代操作
zd = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for k,v in zd.items():
    print(k,":",v)
#判断一个对象是否可以迭代
from collections import Iterable
print(isinstance(1234,Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for i,value in enumerate(['成功','失败','骄傲','谦虚']):
    print(i,value)

