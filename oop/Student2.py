__author__ = 'mocy'
#coding:UTF-8
class Student(object):
    __count = 0
    def __init__(self, name):
        Student.__count = Student.__count + 1
        self.name = name
        print (Student.__count)
s1 = Student('1')
s2 = Student('2')
s3 = Student('3')
s4 = Student('4')
s5 = Student('5')