def calculator(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


@calculator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    else:
        return first / second


print(calc(1, 1))
print(calc(2, 5))
print(calc(6, 3))
print(calc(-1, 0.2))
print(calc(3, (-10)))  # в выводе 13, вместо -30, не могу понять причину
