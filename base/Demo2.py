__author__ = 'mocy'
#coding:UTF-8
#Number（数字）String（字符串）List（列表）Tuple（元组）Sets（集合）Dictionary（字典）
#数据类型:
# 整数
zs = 0x12;#16进制表示整数
print(zs)
# 浮点数
fds = 12.66
print(fds)
# 字符串  '' 和“”当前区别是“”在某些特殊的字符输出时需要转义，如:换行 制表符
#格式化输出语句
zfc1 = 'hello'
zfc2 = "你好"
print(zfc1,zfc2)
zfc3 = "\tyou!"
zfc4 = '\nyou!'
print(zfc3)
print(zfc4)
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# 布尔值 取值：True  False
is_man = True
is_alive = False
print(is_man,is_alive)
# 空值
kz = None
print(kz)
# 列表
list1 = ['abcd', 786 , 2.23, 'runoob', 70.2 ]
print(list1[-1])#获取最后一个元素
list1.append('admin')#追加元素到末尾
print(list1)
list1.insert(1,12)#追加元素到指定位置
print(list1)
list1.pop()#删除末尾的元素,使用pop(i)可以删除指定位置的元素
print(list1)
#元组
yz = ('hello',125,True)
print(yz)
print(yz[0])
# 字典
zd = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(zd)
zd['Michael'] = 90#重新赋值
print(zd)
is_save = 'Bob' in zd #判断key是否存在
print(is_save)
value = zd.get('Tracy')#get获取值
print(zd.get('dd','不存在'))#不存在指定值为不存在
print(value)
#pop('Bob')删除key
#set
s = set([1, 2, 3])    #初始化时提供一个list作为输入集合
s.add(4)              #使用add方法添加元素
s.remove(2)           #使用remove方法
print(s)

print('------------------------------------')
#删除字典元素
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
del dict['Name']; # 删除键是'Name'的条目
print(dict)
dict.clear();     # 清空词典所有条目
print(dict)
del dict ;        # 删除词典
print(dict)
#1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
#2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行.
