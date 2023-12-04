for number in range(1, 101):
    if number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 5 == 0 and number % 3 == 0:
        print('Fuzzbuzz')
    else:
        print(number)
        
