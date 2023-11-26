# Задание 1
# Дан такой список:

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]
print(name, last_name, city, phone, country)

# Задание 2
# Допустим, какая-то программа возвращает результат своей работы в таком виде:

string1 = "результат операции: 42"
string2 = "результат работы программы: 547"
string3 = "результат: 5"

# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# результат сложения распечатайте.

# operation_result = string1.index('42')
# operation_result = int(string1[20:]) - решение исходя из курса урока
operation_result = int(string1[-2:]) + 10  # более короткое решение
print(operation_result)

# work_result = string2.index('547')
# work_result = int(string2[28:]) - решение исходя из курса урока
work_result = int(string2[-3:]) + 10  # более короткое решение
print(work_result)

# result = string3.index('5') #- решение исходя из курса урока
# result = int(string3[11:]) #- решение исходя из курса урока
result = int(string3[-1:]) + 10  # более короткое решение
print(result)

# Задание 3
# Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}.")
