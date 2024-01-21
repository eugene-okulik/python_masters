first_result_line = 'результат операции: 42'
first_result_number_index = first_result_line.index(':')
final_1st_number = first_result_line[first_result_number_index + 1:]
final_1st_number_int = int(final_1st_number)
first_final_result = final_1st_number_int + 10
print(first_final_result)

second_result_line = 'результат операции: 547'
second_result_number_index = second_result_line.index(':')
final_2nd_number = second_result_line[second_result_number_index + 1:]
final_2nd_number_int = int(final_2nd_number)
second_final_result = final_2nd_number_int + 10
print(second_final_result)

third_result_line = 'результат операции: 5'
third_result_number_index = third_result_line.index(':')
final_3rd_number = third_result_line[third_result_number_index + 1:]
final_3rd_number_int = int(final_3rd_number)
third_final_result = final_3rd_number_int + 10
print(third_final_result)
