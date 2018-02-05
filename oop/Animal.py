__author__ = 'mocy'
#coding:UTF-8
class Animal(object):
    def run(self):
        print('Animal is running...')
class Cat(Animal):
    pass
class Dog(Animal):
    pass
cat = Cat()
cat.run()