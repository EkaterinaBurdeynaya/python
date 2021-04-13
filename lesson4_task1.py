from sys import argv

file_name, work_hour, payment, bonus = argv

print(f'your file - {file_name}')
print(f'your working hours are - {work_hour}')
print(f'your payment per hour is - {payment}')
print(f'your bonus is - {bonus}')

salary = float(work_hour) * float(payment) + float(bonus)
print(f"Your salary is {salary}")