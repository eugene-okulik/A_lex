text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

new_txt = []

for word in text.split():
    if ',' in word:
        word = word.replace(',', '') + 'ing,'
    elif '.' in word:
        word = word.replace('.', '') + 'ing.'
    else:
        word += 'ing'
    new_txt.append(word)

print(' '.join(new_txt))
