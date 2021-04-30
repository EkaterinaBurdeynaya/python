class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(int(i))

        return my_date[0], my_date[1], my_date[2]

    @staticmethod
    def valid(day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(int(i))

        if 1 <= my_date[0] <= 31:
            if 1 <= my_date[1] <= 12:
                if 2021 >= my_date[2] >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('30-04-2021')
print(today)
print(Data.valid('30-04-2021'))
print(today.valid('30-04-2021'))
print(Data.extract('30-04-2021'))
print(today.extract('30-04-2021'))
print(Data.valid('30-04-2021'))