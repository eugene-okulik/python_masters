"""Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь"""

import math

a = 5
b = 6

area = a * b / 2
hypotenuse = math.sqrt(a ** 2 + b ** 2)

print(f'Площадь прямоугольного треугольника равна -  {area}')
print(f'Длина гипотенузы прямоугольного треугольника равна - {hypotenuse}')
