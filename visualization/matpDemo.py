__author__ = 'mocy'
#coding:UTF-8

import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
squares = [1,4,8,16,5]
plt.plot(squares,linewidth=1,color='r')#线条粗细
plt.title(u'气温变化表',fontsize=24)
plt.xlabel(u'号',fontsize=12)
plt.ylabel(u'温度/摄氏度',fontsize=12)
plt.tick_params(axis='both',labelsize=12)
plt.show()