def my_func():
    try:
        x = (int(input('input positive number - ')))
        y = (int(input('input counting neg number - ')))
        while x <= 0 or y >= 0:
            x = (int(input('input POSITIVE number - ')))
            y = (int(input('input COUNTING NEG number - ')))
    except ValueError:
        print('data is incorrect')
        return
    deg = x ** y
    return deg

print(my_func())

def my_func():
    try:
        x = (int(input('input positive number - ')))
        y = (int(input('input counting neg number - ')))
        while x <= 0 or y >= 0:
            x = (int(input('input POSITIVE number - ')))
            y = (int(input('input COUNTING NEG number - ')))
    except ValueError:
        print('data is incorrect')
        return
    i = 1
    for i in range(abs(y)+1):
        deg = x ** -i
        i += 1
    return deg

print(my_func())
