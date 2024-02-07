import datetime

file_path = "homework/eugeny_okulik/hw_15/data.txt"

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split('-')
            date_str = parts[1].strip()
            action = parts[2].strip()
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            # Далее можно выполнить необходимые действия в зависимости от даты и текста после даты
            # Например:
            if action == "do something":
                # выполнить действие
                pass
            elif action == "do something else":
                # выполнить другое действие
                pass
            # и так далее

except FileNotFoundError:
    print("Файл не найден.")
except IndexError:
    print("Структура файла некорректна.")
except ValueError:
    print("Некорректный формат даты.")
