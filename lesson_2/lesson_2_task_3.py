import math

sq = int(float(input('Введите сторону квадрата: ')))

def square(sq):
        print(sq*sq)
        sq = math.ceil(sq)
square(sq)