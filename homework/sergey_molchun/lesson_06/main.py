# Задание 1
# Дан такой список:

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
name, last_name, city, phone, country = person

print(f"Name:{name}, Last Name:{last_name}, City:{city}, Phone:{phone}, Country:{country}")

# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:

string1 = "результат операции: 42"
string2 = "результат работы программы: 547"
string3 = "результат: 5"

# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

# TODO: String #1
separator = string1.index(':')
operation_result = int(string1[separator + 1:])  # - решение исходя из курса урока
print(operation_result + 10)

operation_result2 = int(string1[-2:]) + 10  # более короткое решение
print(operation_result2)

# TODO: String #2
separator = string2.index(':')
work_result1 = int(string2[separator + 1:]) + 10  # - решение исходя из курса урока
print(work_result1)

work_result2 = int(string2[-3:]) + 10  # более короткое решение
print(work_result2)

# TODO: String #3
separator = string3.index(':')  # - решение исходя из курса урока
result1 = int(string3[separator + 1:]) + 10  # - решение исходя из курса урока
print(result1)

result2 = int(string3[-1:]) + 10  # более короткое решение
print(result2)

# Задание 3
# Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}.")
