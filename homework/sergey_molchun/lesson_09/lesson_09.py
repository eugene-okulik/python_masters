import sys

sys.set_int_max_str_digits(150000)

# TODO: Напишите функцию-генератор, которая генерирует список чисел фибоначчи
#  Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число


required_fibonnacci_sequense_numbers = [5, 200, 1000, 100000]
counter = 3
required = required_fibonnacci_sequense_numbers[0]


def fibonacci_generator():
    numbers = [1, 1]
    while True:
        number = sum(numbers)
        yield number
        numbers.pop(0)
        numbers.append(number)


for x in fibonacci_generator():
    if counter == required:
        print(f"The {required}-th number in fibonacci sequense is {x}.")
        print(f"The number is {len(str(x))} digits long.\n")

        required_fibonnacci_sequense_numbers.pop(0)
        if len(required_fibonnacci_sequense_numbers) > 0:
            required = required_fibonnacci_sequense_numbers[0]
        else:
            break
    counter += 1


# TODO: Alternative way to calculate Fibonacci:

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


result = fibonacci_iterative(100000)
print(f"Alternative way 100000th: {result}")
print(f"Alternative way lenght: {len(str(result))}")
