__author__ = 'mocy'
#coding:UTF-8
import math
help(abs)#交互式命令查看函数的帮助信息
#取绝对值
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(12))
#在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny
result = move(0,0,5)
print(result)
#默认参数 这是一个求几次方的函数
def power(m,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*m
    return s
print (power(5))
print (power(5,4))



