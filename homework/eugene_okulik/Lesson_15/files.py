import os

# data_file = open('data.txt')
# print(data_file)
# data_file.close()


# with open('data.txt') as file_data:
#     print(file_data.read() / 10)


with open('data2.txt', 'w') as file_to_write:
    file_to_write.write('some string')

# with open('data2.txt', 'w') as file_to_write2:
#     file_to_write2.write('another string')

with open('data2.txt', 'a') as file_to_append:
    file_to_append.write('append string')
    words = ['one\n', 'two\n', 'three\n']
    file_to_append.writelines(words)

current_path = os.path.dirname(__file__)
path_to_file = os.path.join(current_path, 'data.txt')
# print(path_to_file)

# path_to_file = f'{current_path}\\data.txt'


with open(path_to_file, encoding='utf-8') as file_data2:
    # print(file_data2.read())
    # print([x.strip('\n') for x in file_data2.readlines()])
    for _ in range(3):
        print(file_data2.readline())


repo_home = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
# print(repo_home)
eg_file = os.path.join(repo_home, 'homework', 'evgeny_gusinets', 'file.txt')

with open(eg_file, encoding='utf-8') as text_file:
    print(text_file.read())

print(os.getcwd())
print(os.path.dirname(__file__))
