class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'bad year'
            else:
                return f'bad month'
        else:
            return f'bad day'

    def __str__(self):
        return f'current date {Data.extract(self.day_month_year)}'


today = Data('29 - 1 - 2021')
print(today)
print(Data.valid(19, 3, 2012))
print(today.valid(5, 5, 20))
print(today.extract('17 - 09 - 2019'))
print(Data.valid(1, 12, 2019))
print(Data.valid(1, 12, 2020))