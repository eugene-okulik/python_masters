# Дан такой список:
# person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# С помощью распаковки создайте из этого списка переменные, содержащие соответствующие данные:
# name, last_name, city, phone, country

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(f'His name is {name} {last_name}. His phone number is {phone}. He lives in {city}, {country}.')

# Задание 2
# Допустим, какая - то программа возвращает результат своей работы в таком виде:
# результат операции: 42
# результат работы программы: 547
# результат: 5
# С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу
# 10, результат сложения распечатайте.

str1 = 'результат операции: 42'
str2 = 'результат работы программы: 547'
str3 = 'результат: 5'

print(int((str1[20:])) + 10)
print(int(str2[28:]) + 10)
print(int(str3[11:]) + 10)

# Задание 3 Даны такие списки:
# students = ['Ivanov', 'Petrov', 'Sidorov']
# subjects = ['math', 'biology', 'geography']
# Распечатайте текст, который будет использовать данные из этих списков.Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geograpy

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
