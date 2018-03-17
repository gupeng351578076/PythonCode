__author__ = 'mocy'
#coding:UTF-8
class Student(object):
    def __init__(self,name,score):
        self.__name = name#加上两个下划线表示该成员变量私有化
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print__score(self):
        print('%s: %s' % (self.__name, self.__score))
bart = Student('Bob',66)
print(bart.print__score())
print(bart.get_name())