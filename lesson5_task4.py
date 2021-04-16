with open ('lesson5_task4.txt', 'r') as f:
    new_file = open('newlesson5_task4.txt', 'w', encoding='utf-8')
    new_file.close()
    new_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for line in f:
        key, value = line.split(' - ')
        new_file = open('newlesson5_task4.txt', 'a', encoding='utf-8')
        new_key = new_dict[key]
        new_file.write(f'{new_key} - {value}')