# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

# Задание 2

str1 = 'результат операции: 42'
str2 = 'результат работы программы: 547'
str3 = 'результат: 5'

print(int((str1[20:])) + 10)
print(int(str2[27:]) + 10)
print(int(str3[11:]) + 10)


# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(f'Students {",".join(students)} study these subjects: {",".join(subjects)}')

