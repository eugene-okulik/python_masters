from datetime import datetime
date_str = "jan 15, 2023 - 12:05:33"
date = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")
month_name = date.strftime("%B")
print(month_name)

formatted_date = date.strftime("%d.%m.%Y, %H:%M")
print(formatted_date)



