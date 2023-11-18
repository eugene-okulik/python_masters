final_text = '''
Hello {}! You're out of money to buy a {} :(
You need {} dollars more
Possibility to complete this purchase: {}.
{} months left to complete this purchase
'''

final_lucky_text = '''
Hello {}! You can afford to buy a {}!
Possibility to complete this purchase: {}
Congratulations!
'''

q_1 = input('Whats your name?')
q_2 = input('What do you want to buy?')
q_3 = input('How much does it cost?')
q_3 = int(q_3)
q_4 = input('How much do you have?')
q_4 = int(q_4)
q_5 = input('How much money can you deposit per month?')
q_5 = int(q_5)
a_3 = (q_3 - q_4)
a_4 = q_3 <= q_4
a_5 = ((q_3 - q_4) // q_5)

if q_3 > q_4:
    print(final_text.format(q_1, q_2, a_3, a_4, a_5))
if q_3 <= q_4:
    print(final_lucky_text.format(q_1, q_2, a_4))
