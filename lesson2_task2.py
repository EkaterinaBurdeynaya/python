initial_list = list(input('Please enter the elements of your custom list separated by commas - ').split())
list_1 = []

for element in initial_list:
    if element.isdigit() == True:
        element = int(element)
        list_1.append(element)

print(list_1)
list_2 = []

if len(list_1) % 2 == 0:
    element = 0
    while element < len(list_1):
        list_2.append(list_1[element+1])
        list_2.append(list_1[element])
        element += 2
else:
    element = 0
    while element < len(list_1) - 1:
        list_2.append(list_1[element+1])
        list_2.append(list_1[element])
        element += 2

print(list_2)

