def summ():
    result = 0
    while True:
        numbers = list(input('please input numbers - ').split())
        if numbers == '@':
            break
        if '@' in numbers:
            numbers.remove('@')
        for number in map(int, numbers):
            result += number
        print(result)
    return

summ()
