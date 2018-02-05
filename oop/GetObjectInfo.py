__author__ = 'mocy'
#coding:UTF-8
class Driver(object):
    pass
class DrunkDriver(Driver):
    pass
class Teacher(object):
    pass

d = Driver()
print(type(Driver))#打印Driver的信息
print(d)

print('------------types测试----------')
import types
#定义空函数
def hello():
    pass
print(types.FunctionType==type(hello))
print(type(lambda x:x*x)==types.LambdaType)
print(type(hello)==types.GeneratorType)

print('------------isinstance测试----------')
teacher = Teacher()
drunkdriver = DrunkDriver()
print(isinstance(teacher,Driver))
print(isinstance(drunkdriver,Driver))

print('------------dir()测试----------')
list_dir = dir('abc')
print(list_dir)
print(dir(teacher))