from datetime import datetime

date_str = input("Введите дату в формате YYYY-MM-DD: ")

try:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    print("Дата введена верно!", date)
except ValueError:
    print("Неправильный формат. Дату нужно вводить как YYYY-MM-DD, пример 2024-01-10")
