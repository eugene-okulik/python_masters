import os

current_path = os.path.dirname(__file__)
repo_home = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
target_file = os.path.join(
    repo_home, "homework", "eugene_okulik", "Lesson_16", "hw", "data.log"
)

with open(target_file, "r") as file:
    log_list = file.readlines()

log_dict = {}
for data_line in log_list:
    key = data_line.split("::")[0].strip()
    val = data_line.replace("\n", "").replace("  ", " ")
    log_dict.update({key: val})

print(log_dict)
