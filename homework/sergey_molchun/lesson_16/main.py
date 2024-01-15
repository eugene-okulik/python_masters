import os.path

CURRENT_PATH = os.path.dirname(__file__).replace(r"\sergey_molchun\lesson_16", "")
TARGET_PATH = fr"{CURRENT_PATH}\eugene_okulik\Lesson_16\hw"
TARGET_FILE = os.path.join(TARGET_PATH, "data.log")

with open(TARGET_FILE, 'r', encoding="UTF-8") as log_file:
    elements = log_file.readlines()

new_dict = {}

for element in elements:
    dict_key = element.split("  ")[0]
    element = element.replace("\n", "")
    new_dict.update({dict_key: element})

print(new_dict)
