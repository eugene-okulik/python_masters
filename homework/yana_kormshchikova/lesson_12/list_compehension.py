PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_price_list = list(map(lambda x: x.split(' '), PRICE_LIST.replace('p', ' ').splitlines()))
print(new_price_list)

price_dict = {}
for item, price in new_price_list:
    new_price = int(price.replace('р', ''))
    price_dict[item] = new_price

print(price_dict)


