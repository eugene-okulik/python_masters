import csv
import os

base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
path = os.path.join(base_path, 'homework', 'eugene_okulik', 'Lesson_19', 'example.csv')

with open(path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data1 = []
    for row in file_data:
        data1.append(row)

print(data1)


with open(path, newline='') as csv_file2:
    file_data = csv.DictReader(csv_file2)
    data2 = []
    for row in file_data:
        data2.append(row)

print(data2)


with open('new_file.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    # writer.writerow(['1', 'Ivan', 'QWE2', 'M'])
    writer.writerows(data1)


with open('new_file2.csv', 'w') as csv_file:
    # headers = ['Number', 'Name', 'Group', 'gender']
    headers = list(data2[0].keys())
    writer = csv.DictWriter(csv_file, headers)
    writer.writeheader()
    writer.writerows(data2)
