import random

# Задание №1 - "Угадайка"
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
#
# Подсказка: задание выполняется с помощью цикла while

# TODO: Original homework.
# lower_edge = 0
# upper_edge = 10
# number_guessed = False
# number = random.randint(lower_edge, upper_edge)
#
# user_guess = int(input(f"Guess the hidden number! It's in range:{lower_edge} - {upper_edge}.\n"))
# while number_guessed is False:
#     if user_guess < number:
#         user_guess = int(input("Your guess is below the hidden number. Try again!\n"))
#     elif user_guess > number:
#         user_guess = int(input("Your guess is above the hidden number. Try again!\n"))
#     else:
#         print(f"CONGRATULATIONS! Your guess is correct! It was {number}.")
#         number_guessed = True
# print("See you next time ...")


# TODO: Improved homework
lower_edge = 0
upper_edge = 10
game_is_on = True

while game_is_on is True:
    number_guessed = False
    number = random.randint(lower_edge, upper_edge)
    user_guess = int(input(f"Guess the hidden number! It's in range:{lower_edge} - {upper_edge}.\n"))
    while number_guessed is False:
        if user_guess < number:
            user_guess = int(input("Your guess is below the hidden number. Try again!\n"))
        elif user_guess > number:
            user_guess = int(input("Your guess is above the hidden number. Try again!\n"))
        else:
            print(f"CONGRATULATIONS! Your guess is correct! It was {number}.")
            another_game = input("Wanna play again? (Y/N)\n").lower()
            number_guessed = True
            if another_game in ('y', 'yes'):
                continue
            else:
                game_is_on = False
print("See you next time ...")
