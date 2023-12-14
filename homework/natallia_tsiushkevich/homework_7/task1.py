text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero.')
words = text.split()
new_words = []

for word in words:
    if word.endswith(','):
        new_words.append(word.replace(",", "ing,"))
    elif word.endswith('.'):
        new_words.append(word.replace(".", "ing."))
    else:
        new_words.append(word + "ing")

new_text = ' '.join(new_words)
print(new_text)
