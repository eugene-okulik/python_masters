# Задание №1
# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
orig_list = """Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
facilisis vitae semper at, dignissim vitae libero""".split()
# и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова.
# Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
# но уже преобразованного.

updated_list = []
for word in orig_list:
    if word.endswith(',') or word.endswith('.'):
        updated_list.append(f"{word[:-1] + 'ing' + word[-1:]}")
    else:
        updated_list.append(word + "ing")

print(' '.join(updated_list))
