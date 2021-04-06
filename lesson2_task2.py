#option 1

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

#option 2

initial_list = []
for i in range(int(input('Please enter the number of elements in your custom list: '))):
    initial_list.append(int(input('Enter the element (number): ')))
list_1 = initial_list

print(list_1)

element = 0
for i in range(int(len(list_1) // 2)):
    list_1[element], list_1[element + 1] = list_1[element + 1], list_1[element]
    element += 2

print(list_1)
