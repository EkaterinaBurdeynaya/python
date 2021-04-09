def my_func(a, b, c):
    list = [a, b, c]
    summ = list.pop(list.index(max(list))) + max(list)
    return summ

print(my_func(80, 50, 40))