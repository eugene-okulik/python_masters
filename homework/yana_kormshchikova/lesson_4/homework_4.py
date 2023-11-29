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
