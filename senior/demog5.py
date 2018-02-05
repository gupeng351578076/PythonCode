__author__ = 'mocy'
# coding:UTF-8
from functools import reduce
#1 map函数接受两个参数 第一个参数是一个函数第二个参数是一个iterable,函数将作用在每一个序列元素上，返回一个全新的序列
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6])
print(r)
print (list(r))
#2 reduce函数把结果和序列的下一个元素做累积计算
def re(x,y):
    return x*y
print(reduce(re,[1,2,3,4]))
#序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7]))