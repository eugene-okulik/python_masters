import json


class CountryData:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self.__comfort = self.__is_comfort()

    @property
    def data(self):
        return self.__data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self.__comfort

    def __read_file(self):
        file_data = open(self.__filename)
        data = json.load(file_data)
        return data

    def __is_comfort(self):
        return self.__avg_temp >= 20


data1 = CountryData('data1.txt')
print(data1.data)
