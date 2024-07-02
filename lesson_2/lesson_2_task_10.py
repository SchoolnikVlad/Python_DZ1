import math

x = int(input('Минимальная сумма вклада 100 рублей. Введите сумму вклада: '))
if x < 100:
    x = 100

y = int(input('Минимальный срок 1 год. Максимальный 99 лет. Введите срок вклада: '))
if y < 1:
    y = 1
if y > 99:
    y = 99

def bank():
    stavka = 0.1
    sum = x*(1+stavka)**y
    print("По итогу вы получаете", math.floor(sum) , "рублей")
bank()