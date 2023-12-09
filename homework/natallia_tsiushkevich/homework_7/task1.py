text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
add = 'ing'
words = text.split()
for word in words:
    if word.endswith(','):
        word = word.strip(',')
new_text = [word + add for word in words]
sentence = ", ".join(new_text)
print(sentence)
# не знаю как убрать и потом расставить запятыев нужных местах
