number = 7

guess = int(input("Угадайте цифру от 1 до 10: "))

while guess != number:
    print("Попробуйте снова")
    guess = int(input("Угадайте цифру от 1 до 10: "))

print("Поздравляю! Вы угадали!")
