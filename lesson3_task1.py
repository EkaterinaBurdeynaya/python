def division():
    try:
        a = (int(input('input divisiable number - ')))
        b = (int(input('input divisor number - ')))
        while b == 0:
            b = (int(input('input divisor number (cant be 0) - ')))
    except ValueError:
        print('You have to input number')
        return
    div = round(a / b, 2)
    return div

print(division())


