my_list = [7, 5, 3, 3, 2]

new_el = input('Please enter new element for the list - ')


while not new_el.isdigit() == True or int(new_el) < 0:
    new_el = input('Please enter new element for the list (COUNTING NUMBER) - ')

new_el = int(new_el)

for el in range(len(my_list)):
    if new_el > my_list[el]:
        my_list.insert(el, new_el)
        break
    elif new_el <= my_list[-1]:
        my_list.append(new_el)
        break
    el += 1

print(my_list)