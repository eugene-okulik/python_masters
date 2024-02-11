import requests
import datetime as dt

# TODO: Task 1:
# Чтение файлов
# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: (
#         homework/eugeny_okulik/hw_15/data.txt)
# Файлик не копируйте и никуда не переносите.
# Напишите программу, которая читает этот файл, находит в нём даты и делает с этими датами то,
# что после них написано. Опирайтесь на то, что структура каждой строки одинакова:
# сначала идет номер,
# потом дата,
# потом дефис и
# после него текст.
# У вас должен получиться код, который находит даты и для даты под номером один в коде
# должно быть реализовано то действие, которое написано в файле после этой даты.
# Ну и так далее для каждой даты.

response = requests.get(
    "https://github.com/eugene-okulik/python_masters/tree/main/homework/eugene_okulik/hw_15/data.txt")
payload = response.json()['payload']
item_list = (payload['blob']['rawLines'])

dates = []

for elem in item_list:
    # print(elem)
    elem = str(elem)[3:29]
    date = dt.datetime.strptime(elem, "%Y-%m-%d %H:%M:%S.%f")  # 2023-12-04 20:34:13.212967
    # print(elem)
    dates.append(date)

# 1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже.
# Должно получиться 2023-12-04 20:34:13.212967
print(f"Original date: {dates[0]}.")
print(f"Date +7 days: {dates[0] + dt.timedelta(days=7)}.\n")

# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
print(f"{str(dates[1])[:10]} is a - {dates[1].strftime('%A')}.\n")

# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата
date_now = dt.datetime.now()
date_compared = dates[2]
difference = date_now - date_compared
print(f"It's difference of: {difference.days} days.\n")

# TODO: Task 2
# Попросите пользователя ввести дату и
# попробуйте преобразовать дату в формат питона.
# В случае, если пользователь не угадал с форматом ввода даты,
# вы получите исключение.
# Обработайте это исключение и подскажите пользователю в каком формате нужно вводить дату.


date_format_correct = False

while date_format_correct is False:
    user_date = input("Please enter the date of your birth:")

    try:
        date_converted = dt.datetime.strptime(user_date, "%Y-%m-%d")

    except ValueError as em:
        print(f"Error: {em}.")
        print("Please use format: YYYY-MM-DD.\n")

    else:
        date_format_correct = True
        print("You've entered date correctly! Thank YOU!")

print(
    f"Date of your birth: day {date_converted.day} of {date_converted.strftime('%B')} "
    f"of year {date_converted.year}.\n")
