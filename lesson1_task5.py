expenses = int(input('Please enter expenses = '))
income = int(input('Please enter income = '))

if income > expenses:
    print('Your company has profit')
    profit = income - expenses
    print('Profitability of your company - {}'.format(round(profit/income, 2)))
elif income < expenses:
    print('Your company has negative profit')

staff = int(input('Please enter the number of personnel - '))
print('Profit per person in your company - {}'.format(round(income/staff, 2)))