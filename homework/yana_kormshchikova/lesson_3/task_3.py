"""Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел"""

import math

a = 4
b = 13

avr = (a + b) / 2
geometr = math.sqrt(a * b)

print(f'Среднее арифметическое чисел {a} и {b} - {avr}')
print(f'Среднее геометричесое чисел = {geometr}')
