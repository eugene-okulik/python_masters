text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
       "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
text_1 = text.split()

text_final = []

for word in text_1:
    if word.endswith(','):
        text_final.append(f"{word[:-1] + 'ing' + word[-1:]}")
    elif word.endswith('.'):
        text_final.append(f"{word[:-1] + 'ing' + word[-1:]}")
    else:
        text_final.append(word + 'ing')

print(' '.join(text_final))
