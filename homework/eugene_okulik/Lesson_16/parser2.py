with open('data.txt') as data_file:
    data = data_file.read()


sections = data.split('\n\n')

features = {}
for section in sections:
    options_list = section.splitlines()
    categ_title, *values = options_list
    features[categ_title] = values


print(features)
