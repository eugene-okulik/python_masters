# Напишите программу, которая спрашивает:
#
# как вас зовут?
# что вы хотите купить?
# сколько это стоит?
# сколько у вас есть?
# сколько можете отложить в месяц?
# В результате программа должна распечатать, например, такое:
#
# Привет, Петя. На покупку Ferrari тебе не хватает 1000000
#
# Возможность совершения покупки: False
#
# До покупки осталось 200 месяцев

name = input('What is your name? ')
items = input('What do you want to buy? ')
price = int(input('How much does it cost? '))
savings = int(input('How much savings do you have? '))
monthly_save = int(input('How much you may save per month? '))

if price <= savings:
    print(f"Hi {name}! "
          f"For now you can buy {items}. "
          f"Congratulations!"
          )
else:
    print(f"Hi {name}!"
          f"For now you can't buy {items}. "
          f"You need {price - savings} more. "
          f"You need to save for another {((price - savings) // monthly_save)} months to buy")
