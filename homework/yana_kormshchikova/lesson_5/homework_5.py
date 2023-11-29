my_dict = {
    "tuple": (1, 3, 5, 7, 9),
    "list": [1, 5, 6, 7, 4],
    "dict": {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
    "set": {1, 2, 3, 4, 5}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(10)
my_dict['list'].remove(5)

my_dict['dict']['i am a tuple'] = 'no'
my_dict['dict'].pop('key3')

my_dict['set'].add(6)
my_dict['set'].remove(3)

<<<<<<< HEAD
=======

>>>>>>> d0942a26667cc1d133982dc1feb2d225a6286edd
print(my_dict)
