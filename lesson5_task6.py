dict_lessons = {}

with open('lesson5_task6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        hours_list = [i for i in stats if i == ' ' or (i >= '0' and i <= '9')]
        hours_sum = sum(map(int, ''.join(hours_list).split()))
        dict_lessons[name] = hours_sum

print(f"{dict_lessons}")