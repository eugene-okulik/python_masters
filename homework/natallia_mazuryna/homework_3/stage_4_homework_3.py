a = 7
b = 4
c = ((a ** 2 + b ** 2) ** 0.5)
print(c)
p = ((a + b + c) / 2)
s = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
print(s)
