__author__ = 'mocy'
#coding:UTF-8
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()
# def now():
#     print ('now')
# f = now
# print(now.__name__)
# print(f.__name__)
#现在，假设我们要增强now()函数的功能，
#比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

