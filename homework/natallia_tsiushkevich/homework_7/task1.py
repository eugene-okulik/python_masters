text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
add = 'ing'
words = text.split()
for word in words:
        if word.endswith(','):
                word.replace(',', '')  # как удалить запятые?
new_text = [word + add for word in words]
# добавить запятые как?
sentence = " ".join(new_text)
print(sentence)
