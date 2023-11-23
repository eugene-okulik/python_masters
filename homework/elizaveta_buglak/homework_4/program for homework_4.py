import sys
cost_purchase = 1000000
amount_save = 5000

username = input('What is your name?')
print(f'Hello, {username}!')

purchase = input('What do you want to buy?')

if purchase == 'Ferrari':
    print('Ok, let\'s analyze your possibilities!')
else:
    print('My program does\'t understand you')
    sys.exit(0)

amount_money = float(input('How much money do you have?'))
if cost_purchase == amount_money:
    buy_purchase = True
    print('Possibility of making purchase', buy_purchase,
          'Congratulations, you can buy car of your dream', sep='\n')

if cost_purchase > amount_money:
    save_money = float(input('How much money can you save?'))
    buy_purchase = False
    print('Possibility of making purchase:', buy_purchase)
    if save_money == amount_save:
        print((int(cost_purchase/amount_save)), 'months left before purchase')
    elif amount_save > save_money:
        print(f'You need to save {amount_save} every month if you want to buy this car in',
              (int(cost_purchase/amount_save)), 'months')
    else:
        print('I don\'t understand you')
