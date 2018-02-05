__author__ = 'mocy'
class FirstClass:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("hello{0}".format(self.name))
class SecondClass(FirstClass):
    def __init__(self,name):
        FirstClass.__init__(self,name)
    def haha(self):
        print("haha{0}".format(self.name))
s = SecondClass("csdnBlog")
s.hello()
s.haha()