__author__ = 'mocy'
#coding:UTF-8
#利用lambda改写奇偶数判断 输出奇数
L = list(filter(lambda x:x%2==1,range(1,20)))
print(L)