my_dict = {
    'tupple': (1, 5, 10, 'hello', True),
    'list': [2, 4, 6, 'Liza', False],
    'dict': {'number': '22', 'name': 'Liza', 'surname': 'Buglak', 'age': '22', 'Belarus': 'True'},
    'set': {3, 6, 9, 'hello', 'how are you?'}
}
# Действия с элементами словаря my_dict:

# 1: Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print(my_dict['tupple'][-1])

# 2: Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_dict['list'].append('Hello everyone')
my_dict['list'].pop(1)

# 3: Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict['dict']['i am a tuple',] = 'new value was added'
my_dict['dict'].pop('surname')

# 4: Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
my_dict['set'].add('True')
my_dict['set'].remove(9)
print(my_dict['set'])

# В конце выведите на экран весь словарь
print(my_dict)
