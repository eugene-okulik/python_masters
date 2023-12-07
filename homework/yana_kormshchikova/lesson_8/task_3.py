line_1 = 'результат операции: 42'
line_2 = 'результат работы программы: 547'
line_3 = 'результат: 5'


def get_result(line):
    num = int(line[line.find(':') + 1:]) + 10
    print(num)


get_result(line_1)
get_result(line_2)
get_result(line_3)
