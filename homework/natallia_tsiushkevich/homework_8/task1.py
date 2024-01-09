number = 3
while True:
    user_input = int(input('Guess the number:'))
    if user_input == number:
        print('Congratulations! You guessed!')
        break
    else:
        print('Try one more time')
