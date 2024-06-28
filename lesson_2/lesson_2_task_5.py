mounth = int(input('введите номер месяца: '))

if mounth < 1:
    mounth = 1
if mounth > 12:
    mounth = 12

def month_to_season(mounth):
    if (mounth == 12 or mounth == 1 or mounth == 2):
        print('Зима')
    if (mounth == 3 or mounth == 4 or mounth == 5):
        print('Весна')
    if (mounth == 6 or mounth == 7 or mounth == 8):
        print('Лето')
    if (mounth == 9 or mounth == 10 or mounth == 11):
        print('Осень')

month_to_season(mounth)