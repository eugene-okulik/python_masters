my_tuple = ('one', 'two', 'three', 'four', 'five')
my_list = [1, 2, 3, 4, 5, 6]
my_dict2 = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
my_set = {True, False, None, 'set', 12}

my_dict = {
    'tuple': my_tuple,
    'list': my_list,
    'dict': my_dict2,
    'set': my_set
}

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
print(my_dict['tuple'][4])

# Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент, удалите второй элемент списка
my_list.append(7)
my_list.pop(1)

# добавьте элемент с ключом ('i am a tuple',) и любым значением, удалите какой-нибудь элемент
my_dict2['i am a tuple'] = 600
del my_dict2[2]

# Для того, что хранится под ключом ‘set’: добавьте новый элемент в множество, удалите элемент из множества
my_set.add(42)
my_set.remove(None)

# В конце выведите на экран весь словарь
print(my_dict)
