all_numbers = list(range(1, 101))
for number in all_numbers:
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    elif number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
