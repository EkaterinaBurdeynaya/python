initial_list = list(input('Please enter the elements of your custom sentence separated by commas - ').split())

# for el in range(len(initial_list)):
#     if len(initial_list[el]) > 10:
#         initial_list[el] = initial_list[el][:9]
#     el += 1

for index, value in enumerate(initial_list, 1):
    print(f'{index}. {value[:10]}')

