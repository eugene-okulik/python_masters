my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4', 'key_5': 'value_5'},
    'set': {'text_1', 'text_2', 'text_3', 'text_4', 'text_5'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('six')
my_dict['list'].pop(1)

my_dict['dict'][('I am a tuple', )] = 'hello'
del my_dict['dict']['key_1']

my_dict['set'].add('Hello')
my_dict['set'].remove('text_1')

print(my_dict)
