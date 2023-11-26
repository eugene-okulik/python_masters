from pprint import pprint

# Создайте словарь  my_dict с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.
my_dict = {
    "tuple": (20, 1, 15, 22, False),
    "list": [1, 2, 10, "Vasi", True],
    "dict": {"name": "Dima", "city": "Ms", "age": 32, "phone": "honor", "lang": "ru"},
    "set": {34.2, -21, 133, "python", "c++"},
}

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
print(my_dict["tuple"][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_dict["list"].append(100)
del my_dict["list"][1]

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict["dict"].update({('i am a tuple',): (2, -1)})
del my_dict["dict"]["city"]

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
my_dict["set"].add("Rust")
my_dict["set"].remove("c++")

pprint(my_dict)