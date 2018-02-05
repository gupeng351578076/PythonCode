__author__ = 'mocy'
#coding:UTF-8
#3 filter函数将传入的函数作用在序列上，判断是否为true，为true保留元素
list3 = [10,20,30,15,25,63]
def fi(x):
    return x%2==0
print (filter(fi,list3))

#对于列表筛选
from random import randint
data = [randint(-10,10) for _ in range(10)]
print(data)
#1循环判断
print ([x for x in data if x>=0])
#2filter函数
def is_odd(x):
    return x%2==1
data1 = filter(is_odd,data)

#对于字典筛选
dataz = {x:randint(60,100) for x in range(1,21)}#得到字典dataz
print(dataz)
#过滤字典分数高于90
def filter_l(data):
    return {k:v for k,v in data.items() if v>90}
new = filter_l(dataz)
print(new,type(new))

#对于集合的筛选
def filter_j(data):
    return {x for x in data if x%3==0}
dataj = {randint(0,100) for x in range(10)}
newj = filter_j(dataj)
print(newj,type(newj))
h = filter(filter_j,dataj)
print(type(h))
