from datetime import datetime

date_object = datetime.strptime("Jan 15, 2023 - 12:05:33", "%b %d, %Y - %H:%M:%S")

print(date_object.strftime("%B"))

print(date_object.strftime("%d.%m.%Y, %H:%M"))
