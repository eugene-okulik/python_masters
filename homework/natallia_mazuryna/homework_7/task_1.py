original_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
                 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words_from_text = original_text.split()
words_modified = []

for word in words_from_text:
    if word.endswith(','):
        modified_word = word[:-1] + 'ing' + ','
    elif word.endswith('.'):
        modified_word = word[:-1] + 'ing' + '.'
    else:
        modified_word = word + 'ing'

    words_modified.append(modified_word)

final_text = ' '.join(words_modified)
print(final_text)
