from functools import reduce

list_1 = [i for i in range (100, 1001) if i % 2 == 0]
print(list_1)

def multi(prev_el, el):
    return prev_el * el

print(reduce(multi, list_1))