__author__ = 'mocy'
#coding:UTF-8
#单例模式的实现有很多方式 1使用模块 2使用装饰器 3使用多线程锁
import threading
#4基于__new__当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__），
#实例化对象；然后再执行类的__init__方法，对这个对象进行初始化
class Singleton(object):
    _instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock:
                Singleton._instance = object.__new__(cls)
        return Singleton._instance
obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)



#5使用metaclass方式实现
# import threading
# class SingletonType(type):
#     _instance_lock = threading.Lock()
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
#         return cls._instance
#
# class Foo(metaclass=SingletonType):
#     def __init__(self,name):
#         self.name = name
#
# obj1 = Foo('name')
# obj2 = Foo('name')
# print(obj1,obj2)