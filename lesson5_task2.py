with open ('lesson5_task2.txt', 'r') as f:
    for num, el in enumerate(f, 1):
        count = 1
        for i in range(len(el)):
            if el[i] == ' ':
                count += 1
        print(f'in {num} line {count} words')

print(f'in this file {num} lines')

