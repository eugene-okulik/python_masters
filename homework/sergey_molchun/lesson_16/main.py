import os.path

"""TODO:
В папке homework/eugene_okulik/Lesson_16/hw лежит файл data.log

Файл не копируйте и никуда не переносите. Прочитайте этот файл и
превратите всё его содержимое в питоновский словарь такого вида:

{
    '2022-05-18 12:19:51.685496': '2022-05-18 12:19:51.685496
     ::WARNING:: Memory is almost full',
    '2022-05-18 12:20:55.783416': '2022-05-18 12:20:55.783416
     ::INFO:: Reading data from disk',
    '2022-05-18 12:20:57.923814': '2022-05-18 12:20:57.923814
     ::ERROR:: No response from disk, data can not be retrieved',
    '2022-05-18 12:20:59.369107': '2022-05-18 12:20:59.369107
     ::ERROR:: Exited abnormally'
}
"""

ROOT_FOLDER = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

TARGET_FILE = os.path.join(ROOT_FOLDER,
                           'eugene_okulik', 'Lesson_16', 'hw', 'data.log')

with open(TARGET_FILE, 'r', encoding="UTF-8") as log_file:
    elements = log_file.readlines()

new_dict = {}

for element in elements:
    dict_key = element.split("  ")[0]
    element = element.replace("\n", "")
    new_dict.update({dict_key: element})

print(new_dict)
