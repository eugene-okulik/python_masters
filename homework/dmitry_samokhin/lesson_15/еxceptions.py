from datetime import datetime

date_str = input("Введите дату в формате YYYY-MM-DD: ")

try:
    date = datetime.strptime(date_str, "%Y-%m-%d")
    print("Дата распарсена успешно!", date)
except ValueError:
    print(f"Неправильный формат. Дату нужно вводить как YYYY-MM-DD, пример 2023-01-15")
