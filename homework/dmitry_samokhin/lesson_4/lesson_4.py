name = input("как вас зовут? ")
product = input("что вы хотите купить? ")
price = float(input("сколько это стоит? "))
available = float(input("сколько у вас есть? "))
save = float(input("сколько можете отложить в месяц? "))

print(
    f"Привет, {name}. На покупку {product} тебе не хватает {price - available}",
    f"Возможность совершения покупки: {available >= price}",
    f"До покупки осталось {(price - available) / save} месяцев",
    sep="\n",
)
