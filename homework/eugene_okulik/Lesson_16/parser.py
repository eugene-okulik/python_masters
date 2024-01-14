with open('data.txt') as data_file:
    data = data_file.read()


lines = data.splitlines()

features = {}

new_categ = True
current_categ = None
for line in lines:
    print(line, new_categ)
    if new_categ:
        features[line] = []
        new_categ = False
        current_categ = line
    elif line == '':
        new_categ = True
        current_categ = None
    else:
        features[current_categ].append(line)

print(features)
