with open ('lesson5_task3.txt', 'r') as f:
    workers = {}
    sum_salary = 0.00
    person = 0
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: salary lower 20000')
        sum_salary += float(value)
        person += 1
    avarage_salary = round(sum_salary/person, 2)
    print(avarage_salary)
