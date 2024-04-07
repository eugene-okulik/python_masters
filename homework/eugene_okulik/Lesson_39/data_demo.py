import json
# from dataclasses import dataclass
from pydantic import BaseModel
from typing import List


# class Data:
#     title = 'h1'
#     button = '#button1'
#     price = '[class="price product"]'
#
#
# data_dict = {
#     'title': 'h1',
#     'button': '#button1',
#     'price': '[class="price product"]',
# }
#
#
# data = Data()
#
# data.price
# data_dict['price']
#
#
# class DataFile:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def read_file(self):
#         with open(self.filename) as data:
#             return data.read()


# @dataclass
class FileData(BaseModel):
    city: str
    temperature: int
    location: List[float]
    clouds: bool = False
    # pass


with open('data_dile.txt') as data_file:
    file_data = data_file.read()
    data = json.loads(file_data)  # {"city": "Belgrade", "temperature": 24, "location": [1.1, 2.2]}
    file_data = FileData(**data)  # city="Belgrade", temperature=24, location=[1.1, 2.2]
    # FileData()


print(file_data.location)
# print()
