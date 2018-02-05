__author__ = 'mocy'
#coding:UTF-8
# print(complex(4,5))
# coment = 'I\'m young'
# print(coment)
# print("young\npeople")
# people = ["zhangsan","lisi"]
# print(people[0])
# names = ("a","b","c")
# print(names[0])
x = 1 #变量赋值定义一个变量x
print(id(x)) #打印变量x的标识
print(x+5) #使用变量
print("=========华丽的分割线=========")
x = 2 #量赋值定义一个变量x
print(id(x)) #此时的变量x已经是一个新的变量
print(x+5) #名称相同，但是使用的是新的变量x

print('变量的作用域问题：局部变量 全局变量')
number1 = 12
def add_num():
    global number1
    number1 = 15
    print(number1)
add_num()
