with open ('lesson5_task5.txt', 'w+') as f:
    list_content = list(input('Please input content - ').split())
    f.writelines(list_content)
    sum = 0

    # print(sum + int(el) for el in list_content)

    for i in list_content:
        sum += int(i)
    print(sum)