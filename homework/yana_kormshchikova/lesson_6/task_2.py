line_1 = 'результат операции: 42'
line_2 = 'результат работы программы: 547'
line_3 = 'результат: 5'

line_1_index = line_1.find(':')
num1 = int(line_1[line_1_index + 1:])+10
line_2_index = line_2.find(':')
num2 = int(line_2[line_2_index + 1:])+10
line_3_index = line_3.find(':')
num3 = int(line_3[line_3_index + 1:])+10


print(num1)
print(num2)
print(num3)
