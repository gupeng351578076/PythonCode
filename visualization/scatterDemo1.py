__author__ = 'mocy'
#coding:UTF-8
# from pylab import *
# import matplotlib.pyplot as plt
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=10)
# plt.title('散点图',fontsize=20)
# plt.xlabel('值',fontsize=12)
# plt.ylabel('横坐标',fontsize=12)
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
 edgecolor='none', s=40)

plt.axis([0, 1100,-200, 1100000])
plt.show()
plt.savefig('squares_plot.png',bbox_inchs='tight')