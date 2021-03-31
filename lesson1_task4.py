num1 = str(input('Please enter your number - '))

lenth = len(num1)
max_sym = 0

for i in range(0, lenth):
    if int(num1[i]) > max_sym:
        max_sym = int(num1[i])

print('The largest digit in the number - {}'.format(max_sym))

num1 = str(input('Please enter your number - '))

lenth = len(num1)
max_sym = 0
i = 0

while i < lenth:
    if int(num1[i]) > max_sym:
        max_sym = int(num1[i])
    i += 1

print('The largest digit in the number - {}'.format(max_sym))

num1 = int(input('Please enter your number - '))
max_sym = num1 % 10
num1 = num1 // 10

while num1 > 0:
    if num1 % 10 > max_sym:
        max_sym = num1 % 10
    num1 = num1 // 10

print('The largest digit in the number - {}'.format(max_sym))