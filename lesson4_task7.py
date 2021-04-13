from math import factorial

def fact(n):
    list = [factorial(i) for i in range(1, n+1)]
    yield list

n = int(input('please input factorial number - '))

for el in fact(n):
    print(el)

