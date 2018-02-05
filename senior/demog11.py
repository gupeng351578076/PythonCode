__author__ = 'mocy'
#coding:utf-8
import functools
int2 = functools.partial(int,base=2)
number = '1000'
print(int('1000',base=2))
number1 = int2(number)
print(number1)