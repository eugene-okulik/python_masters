
name = input('What is your name?')
item = input('What do you want to buy?')
price = int(input('How much does it cost?'))
your_money = int(input('How much money do you have now?'))
month_savings = int(input('How much can you save per month?'))

a = price - your_money                                                    # difference between cost of item and savings
c = (price - your_money) / month_savings                                  # number_of_months_before_purchase

if a <= 0:
    print('Congratulations, ' + name + '! You can buy your dream!')
else:
    a = str(a)
    c = str(c)
    print('Hello, ' + name + '. You do not have ' + a + ' to buy a ' + item + '.')
    print('You can not buy ' + item + ' now. :-(')
    print('But do not be sad! Only ' + c + ' months left until purchase! :-)')
