# dict

season = input('Please enter the number of tne month - ')

while not season.isdigit() == True or int(season) > 12 or int(season) < 1:
    season = input('Please enter the correct number of tne month (from 1 to 12) - ')

season = int(season)
dict_1 = {'winter' : [1, 2, 12], 'spring' : [3, 4, 5], 'summer' : [6, 7, 8], 'fall' : [9, 10, 11]}

# print(dict_1.values())

for key, value in dict_1.items():
    # print(value)
    if season in value:
        print(key)
        break
    # else:
    #     print('next')


# list

season = input('Please enter the number of tne month - ')

while not season.isdigit() == True or int(season) > 12 or int(season) < 1:
    season = input('Please enter the correct number of tne month (from 1 to 12) - ')

season = int(season)
list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
list_season = ['winter', 'spring', 'summer', 'fall']

if season <= 2 or season == 12:
    print(f'The month is {list_month[season - 1]} and the season is {list_season[0]}')
elif 5 >= season >= 3:
    print(f'The month is {list_month[season - 1]} and the season is {list_season[1]}')
elif 8 >= season >= 6:
    print(f'The month is {list_month[season - 1]} and the season is {list_season[2]}')
else:
    print(f'The month is {list_month[season - 1]} and the season is {list_season[3]}')