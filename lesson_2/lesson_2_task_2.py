year = int(input('Введите год: '))

def is_year_leap():
        if (year % 4 == 0):
            print(True)
        else:
            print(False)
is_year_leap()


def is_year_leap(year):
        if (year % 4 == 0):
            print('год', year, True)
        else:
            print('год', year, False)
is_year_leap(year)