km_day = int(input('Please enter how many km the runner did in the first day - '))
km_final = int(input('Please enter which result the runner should achieve - '))

day = 1
print('Result in {} day = {}'.format(day, km_day))

while km_day < km_final:
    km_day = round(km_day * 1.1, 2)
    day += 1
    print('Result in {} day = {}'.format(day, km_day))

print('In {} day the runner achieved {} km'.format(day, km_final))