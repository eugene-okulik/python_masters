text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, ' \
       'dignissim vitae libero'

new_text = text.split()
converted_words = []

for word in new_text:
    if ',' in word:
        new_word = word[0:-1] + 'ing' + word[-1:]
        converted_words.append(new_word)
    elif '.' in word:
        new_word = word[0:-1] + 'ing' + word[-1:]
        converted_words.append(new_word)
    else:
        new_word = word + 'ing'
        converted_words.append(new_word)

print(' '.join(converted_words))
