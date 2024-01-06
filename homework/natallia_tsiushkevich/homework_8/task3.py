a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'


def result(num):
    number = int(num[num.find(':') + 2:])
    print(number + 10)


result(a)
result(b)
result(c)
result(d)
