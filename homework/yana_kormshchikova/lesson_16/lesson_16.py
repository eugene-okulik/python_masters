import os

current_path = os.path.dirname(__file__)
homework_dir = os.path.dirname(os.path.dirname(current_path))
target = os.path.join(homework_dir, "eugene_okulik", 'Lesson_16', 'hw', 'data.log')

print(target)

with open(target, 'r') as file_to_read:
    lines = file_to_read.readlines()

new_dict = {}

for line in lines:
    new_line = line.split('  ')[0]
    element = line.replace("\n", "")
    new_dict.update({new_line: element})

print(new_dict)
