# Task 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(f'{name} {last_name} {city} {phone} {country}')


# Task 2

line_1 = "результат операции: 42"
line_2 = "результат работы программы: 547"
line_3 = "результат: 5"

number_1 = int(line_1[line_1.find(':') + 1:])
number_2 = int(line_2[line_2.find(':') + 1:])
number_3 = int(line_3[line_3.find(':') + 1:])

print(number_1 + 10)
print(number_2 + 10)
print(number_3 + 10)


# Task 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
surname1, surname2, surname3 = students
subject1, subject2, subject3 = subjects
print(f'Students {", ".join(students)} study these subjects: {", ".join(subjects)}')
