with open ('lesson5_task1.txt', 'w') as f:
    while True:
        list_content = input('Please input content - ')
        if list_content == '':
            break
        f.writelines(f'{list_content}\n')

