__author__ = 'mocy'
#coding:UTF-8
#生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listData = list(range(1,11))
for i in listData:
    print(i)
#生成[1x1, 2x2, 3x3, ..., 10x10]
listss = []
for x in range(1,11):
    listss.append(x*x)
print(listss)
#简易写法
listjs = [x*x for x in range(1,100) if x%2==0]
print(listjs)
#生成全排列
pl = [m+n for m in 'abc' for n in 'xyz']
print(pl)
#列出文件和目录名
import os
print([d for d in os.listdir('.')])