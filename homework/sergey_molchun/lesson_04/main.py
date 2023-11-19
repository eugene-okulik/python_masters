# Напишите программу, которая спрашивает:
#
# как вас зовут?
# что вы хотите купить?
# сколько это стоит?
# сколько у вас есть?
# сколько можете отложить в месяц?
# В результате программа должна распечатать, например, такое:
#
# Привет, Петя. На покупку Ferrari тебе не хватает 1000000
#
# Возможность совершения покупки: False
#
# До покупки осталось 200 месяцев

name = input("What is your name? ")
goods = input("What do you want to purchase? ")
goods_price = float(input("How much it cost ($)? "))
your_money = float(input("How much do you have ($)? "))
monthly_deposit = float(input("How much you may deposit monthly ($)? "))

if goods_price <= your_money:
    purchase_possibility = True
else:
    purchase_possibility = False


def purcahse():
    if goods_price < your_money:
        return "can"
    else:
        return "can't"


print(f"\nHello {name}.\n"
      f"Now you {purcahse()} afford this purchase!")

if purchase_possibility is True:
    print(f"For purchasing {goods} you don't need to raise more funds.")
    print("Congratulations!")
else:
    print(f"For purchasing {goods} you need {goods_price - your_money}$ more.")
    print(
        f"Approximate time to raise funds for purchase is {int((goods_price - your_money) / monthly_deposit)} months.")
