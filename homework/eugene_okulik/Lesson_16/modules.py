import random
from homework.eugene_okulik.Lesson_16 import example
from homework.eugene_okulik.Lesson_16 import my_file_with_useful_features as my_f
from homework.eugene_okulik.Lesson_16 import parser as parser1
from homework.eugene_okulik.Lesson_16.subfolder import parser as parser2

print(parser1.line)
print(parser2.line)

print()
# input()

my_list = [1, False, 'text']
print(random.random() * 100)
print(random.randint(1, 2))
print(random.randrange(1, 2))
print(random.choice(my_list))

print(example.my_var)
example.func(5)
my_obj = example.MyClass()
print(my_f.a)
