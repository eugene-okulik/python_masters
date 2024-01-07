import os
from datetime import datetime, timedelta

current_path = os.path.dirname(__file__)
repo_home = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
target_file = os.path.join(repo_home, "homework", "eugene_okulik", "hw_15", "data.txt")


with open(target_file, "r") as file:
    lines = file.readlines()

for line in lines:
    number, date_str = int(line.split()[0][0]), f"{line.split()[1]} {line.split()[2]}"
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    match number:
        case 1:
            new_date = date + timedelta(weeks=1)
            print(new_date.strftime("%Y-%m-%d %H:%M:%S.%f"))
        case 2:
            day = date.strftime("%A")
            print(day)
        case 3:
            now = datetime.now()
            delta = now - date
            print(delta.days)
