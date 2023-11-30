username = input('Как вас зовут?')
purchase = input('Что вы хотите купить?')
price = int(input('Сколько это стоит?'))
amount = int(input('Сколько у вас есть?'))
rest = int(input('Сколько можете отложить в месяц?'))
balance = price - amount
full_text = (f'Привет {username}. Тебе не хватает {balance} на покупку {purchase}.'
             f'Возможность совершения покупки: {amount >= price}.'
             f'до покупки осталось {balance // rest} месяцев'
             )

print(full_text)
