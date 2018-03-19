__author__ = 'mocy'
#encoding:UTF-8
import os

print(os.path.abspath('.'))
#创建一个目录
os.mkdir(os.path.join(os.path.abspath('.'),'newfile'))#os.rmdir('移除的文件目录')
