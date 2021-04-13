from itertools import count, cycle

num = int(input('please input start number - '))

for el in count(num):
    if el > 1000:
        break
    else:
        print(el)


list_1 = ['A', 'B', 'C']

c = 0
for el in cycle(list_1):
    if c > 100:
        break
    print(el)
    c += 1