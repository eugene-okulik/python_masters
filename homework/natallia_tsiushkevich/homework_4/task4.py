username = input('What is your name?')
purchase = input('What do you want to buy?')
price = int(input('How much does it cost?'))
amount = int(input('How much do you have?'))
rest = int(input('How much can you save per month?'))
balance = price - amount
full_text = (f'Hello {username}. You do not have {balance} to buy a {purchase}.\n '
             f'Possibility of making a purchase: {amount >= price}.\n'
             f'{balance // rest} months left until purchase'
             )
print(full_text)
