__author__ = 'mocy'
#coding:UTF-8
data1 = (x*x for x in range(1,11) )
print(data1)
# print(next(data1))
for n in data1:
    print(n)

#斐波拉契数列
print('--------------------------')
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)