def get_result(str):
    index = str.index(':') + 2
    result = int(str[index:]) + 10
    return result


str_1 = 'результат операции: 42'
str_2 = 'результат работы программы: 547'
str_3 = 'результат: 5'

print(get_result(str_1))
print(get_result(str_2))
print(get_result(str_3))
