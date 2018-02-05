__author__ = 'mocy'
#coding:UTF-8
#4sorted:接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print (sorted([15,45,62,78,20],key=abs))

#匿名函数，关键字lambda表示匿名函数，冒号前面x表示函数参数，只能有一个表达式不用谢return
nm = lambda x:x*x*x
print (nm(5))

#引入collections模块
#1 defaultdict表示带有默认值的字典
#原生的dict数据类型在d[key]方式下访问元素时，如果没有对应的key会造成KeyEerror异常
#使用defaultdict时，需要传入一个工程函数，工厂函数会构建类似dict的对象，该对象具有默认值
from collections import defaultdict
from collections import namedtuple
#引入函数操作库operator
from operator import itemgetter
#开始逻辑代码
d = defaultdict(list)
print(d)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
d['b'].append(6)
print(d)
print(d.get("a"))
print(d.keys())
print([d.get(i) for i in d])

#2 namedtuple产生可以使用名称来访问元素的数据对象
Student = namedtuple('Student','id name score')
students = [(1,'wu',90),(2,'zhang',85),(3,'li',98)]
for i in students:
    stu = Student._make(i)
    print (stu)

#通过公共键对字典进行排顺序
data=[
    {'name':'bran','uid':101},
    {'name':'xisi','uid':102},
    {'name':'land','uid':103},
]
#输出按照name排序的结果
print(sorted(data,key=itemgetter("name")))
#输出按照uid排序的结果
print(sorted(data,key=itemgetter("uid")))