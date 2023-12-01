str1 = 'результат операции: 42'
str2 = 'результат работы программы: 547'
str3 = 'результат: 5'

str1_index = str1.find('42')
str1_result = int(str1[str1_index:])
print(str1_result + 10)

str2_index = str2.find('547')
str2_result = int(str2[str2_index:])
print(str2_result + 10)

str3_index = str3.find('5')
str3_result = int(str3[str3_index:])
print(str3_result + 10)
