number = int(input('Please enter time in seconds - '))

hours = number // 3600
minutes = number % 3660 // 60
seconds = number % 3600 % 60

if seconds < 10:
    print('{}:{}:0{}'.format(hours,minutes,seconds))
else:
    print('{}:{}:{}'.format(hours,minutes,seconds))