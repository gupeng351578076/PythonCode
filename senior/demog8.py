__author__ = 'mocy'
#coding:UTF-8
def lazy_sum(*args):
    def sum():
        an = 0
        for n in args:
            an = an+n
        return an
    return sum
f = lazy_sum(12,34,56,78)
print(f)
print(f())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())