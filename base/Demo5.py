__author__ = 'mocy'
#coding:UTF-8
import  keyword
#引入自己开发的const模块
import  util.const
print('const' in keyword.kwlist)#判断const是否是python的关键字
util.const.name = 'zhangsan'
print(util.const.name)
