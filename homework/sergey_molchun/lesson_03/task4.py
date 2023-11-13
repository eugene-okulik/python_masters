import math
# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

x = 9
y = 18

print(f"Length of longest side in right triangle if shortest sides are {x} and {y} is "
      f"{math.sqrt(math.pow(x,2) + math.pow(y,2))}")

print(f"Area of right triangle if shortest sides are {x} and {y} is {x*y/2}")
