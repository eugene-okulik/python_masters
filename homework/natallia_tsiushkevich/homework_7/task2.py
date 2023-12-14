sequence = list(range(1, 101))
for number in sequence:
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fuzz")
    else:
        print(number)

#  с печатью "FuzzBuzz" помог чат gpt, тк я поставила это условие третьим
#  и не распечатывалось правильно,
#  разобралась почему так необходимо написать
