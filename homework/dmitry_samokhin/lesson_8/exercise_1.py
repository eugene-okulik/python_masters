from random import randint

num = randint(1, 10)
while int(input("Угадай число от 1 до 10: ")) != num:
    print("попробуйте снова")

print("Поздравляю! Вы угадали!")
