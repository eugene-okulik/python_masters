# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

# Задание 2

str_1 = 'результат операции: 42'
str_2 = 'результат работы программы: 547'
str_3 = 'результат: 5'

print(int(str_1[str_1.index(':') + 2:]) + 10)
print(int(str_2[str_2.index(':') + 2:]) + 10)
print(int(str_3[str_3.index(':') + 2:]) + 10)


# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {",".join(students)} study these subjects: {",".join(subjects)}')
