my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [12, 22, 33, 44, 55],
           'dict': {'key1': 'test1', 'key2': 'test2', 'key3': 'test3', 'key4': 'test4', 'key5': 'test5'},
           'set': {1, 2, 3, 4, 5}}

print(my_dict['tuple'][-1])

my_dict['list'].append(6)
del my_dict['list'][1]

my_dict['dict'][('i am a tuple')] = 'new test'
del my_dict['dict']['key3']

my_dict['set'].add(6)
my_dict['set'].remove(2)

print(my_dict)
