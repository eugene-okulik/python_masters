a = (1, 'a', 22.2, 'true', 55)
b = [3, 30, 'text', 'false', 33.3]
c = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'}
e = {1, 44, 4, 'worlds', 4, 'bool'}
my_dict = {'tuple': a, 'list': b, 'dict': c, 'set': e}

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент

print(a[-1])

# Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент; удалите второй элемент списка

b.append(2)
print(my_dict['list'])
b.pop(2)
print(my_dict['list'])

# Для того, что хранится под ключом ‘dict’:добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент

c['i am a tuple'] = 'any'
print(my_dict['dict'])
del c['one']
print(my_dict['dict'])

# Для того, что хранится под ключом ‘set’: добавьте новый элемент в множество, удалите элемент из множества

e.add('name')
print(my_dict['set'])
e.pop()
print(my_dict['set'])
print(my_dict)
