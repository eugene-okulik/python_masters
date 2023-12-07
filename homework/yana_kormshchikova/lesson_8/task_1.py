num = 5

user_input = int(input('Guess number from 1 to 10: '))
while user_input != num:
    print("You didn't guess! Try again!")
    user_input = int(input('Enter your number: '))

print('Congratulations! You win!')
