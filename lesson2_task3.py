season = int(input('Please enter the number of tne month - '))

while season > 12 or season < 1:
    season = int(input('Please enter the correct number of tne month (from 1 to 12) - '))

dict_1 = {'winter' : [1, 2, 12], 'spring' : [3, 4, 5], 'summer' : [6, 7, 8], 'fall' : [9, 10, 11]}

# print(dict_1.values())

for key, value in dict_1.items():
    # print(value)
    if season in value:
        print(key)
        break
    # else:
    #     print('next')