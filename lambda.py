# LAMBDA

x = lambda a: a+10
print(x(5))

x = lambda a,b: a*b
print(x(5,6))

x = lambda a,b,c: a+b*c
print(x(1,2,3))


def myfunc(n):
    return lambda a: a*n

mydouble = myfunc(2)
print(mydouble(11))