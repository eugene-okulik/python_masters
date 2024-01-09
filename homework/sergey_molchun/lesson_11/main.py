# TODO: Задание №1
# Создайте универсальный декоратор, который можно будет применить к любой функции. Декоратор должен делать следующее:
# он должен распечатывать слово "finished"после выполнения декорированной функции.
#
# Код, использующий этот декоратор может выглядеть, например, так:
#
# @finish_me
# def example(text):
#     print(text)
# example('print me')
#
# В результате работы будет такое:
# "print me"
# "finished"
#

def finish_me(func):
    def wrapper(*args):
        func(*args)
        print("finished\n")

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')


# Дополнительные задания (необязательные):
# TODO: Задание №2
# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция
#
# Код, использующий этот декоратор может выглядеть, например, так:
##
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=2)
#
# В результате работы будет такое:
# print me
# print me


def repeat_me(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


# Задание №3
# Напишите программу:
# Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....

# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def operation(func):
    def wrapper(operand1, operand2):
        if operand1 == operand2:
            return func(operand1, operand2, "+")
        elif operand1 < 0 or operand2 < 0:
            return func(operand1, operand2, "*")
        elif operand1 > operand2:
            return func(operand1, operand2, "-")
        elif operand1 < operand2:
            return func(operand1, operand2, "/")

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '*':
        return first * second
    elif operation == '-':
        return first * second
    elif operation == '/':
        return first / second


input1 = float(input("Enter first operand:"))
input2 = float(input("Enter second operand:"))

print(calc(input1, input2))
