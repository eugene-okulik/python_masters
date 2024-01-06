import datetime

# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# # Преобразуйте эту дату в питоновский формат, после этого:
# # 1. Распечатайте полное название месяца из этой даты
# # 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
print(datetime.datetime.strftime(python_date, '%B'))
print(datetime.datetime.strftime(python_date, '%b %d, %Y - %H:%M'))
