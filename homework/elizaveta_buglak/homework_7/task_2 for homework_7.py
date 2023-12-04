for num1 in range(1, 101):
    if num1 % 3 == 0:
        print('Fuzz')
    elif num1 % 5 == 0:
        print('Buzz')
    elif num1 % 5 == 0 and num1 % 3 == 0:
        print('Fuzzbuzz')
    else:
        print(num1)
        
