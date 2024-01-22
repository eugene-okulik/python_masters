"""
Этот модуль представляет собой программу,
оторая запрашивает информацию у пользователя о его имени, товаре,
цене товара, имеющихся деньгах и месячных отложениях.
Затем программа определяет, может ли пользователь приобрести товар
и выводит результаты взаимодействия с пользователем,
включая приблизительное время для накопления средств.
"""
import math


def calculate_months_needed(goods_price, your_money, monthly_deposit):
    """
    Вычисляет количество месяцев, необходимых для накопления
    средств на покупку товара.

    Args:
        goods_price (float): Цена товара.
        your_money (float): Сумма денег, которая уже имеется.
        monthly_deposit (float): Сумма, которую можно отложить в месяц.

    Returns:
        int: Количество месяцев, необходимых для накопления средств.
    """
    months_needed = math.ceil((goods_price - your_money) / monthly_deposit)
    return max(0, months_needed)


def get_user_input():
    """
    Запрашивает у пользователя информацию о его имени,
    товаре, его стоимости, имеющихся деньгах и месячных отложениях.

    Returns:
        tuple: Кортеж с данными, включающий имя, товар,
        стоимость, имеющиеся деньги и месячные отложения.
    """
    name = input("Как вас зовут? ")
    goods = input("Что вы хотите купить? ")
    goods_price = float(input("Сколько это стоит ($)? "))
    your_money = float(input("Сколько у вас есть ($)? "))
    monthly_deposit = float(input("Сколько вы можете отложить в месяц ($)? "))

    return name, goods, goods_price, your_money, monthly_deposit


def can_purchase(goods_price, your_money):
    """
    Проверяет, может ли пользователь приобрести товар.

    Args:
        goods_price (float): Цена товара.
        your_money (float): Сумма денег, которая уже имеется.

    Returns:
        bool: True, если пользователь может приобрести товар, False в противном случае.
    """
    return goods_price <= your_money


def display_results(name, goods, goods_price, your_money, purchase_possibility):
    """
    Отображает результаты взаимодействия с пользователем.

    Args:
        name (str): Имя пользователя.
        goods (str): Название товара.
        goods_price (float): Цена товара.
        your_money (float): Сумма денег, которая уже имеется.
        purchase_possibility (bool): Флаг возможности приобретения товара.
    """
    print(f"\nПривет, {name}!")
    price_difference = max(0, goods_price - your_money)
    print(f"На покупку {goods} вам не хватает {price_difference}$")
    print(f"Возможность совершения покупки: {'можете' if purchase_possibility else 'не можете'}")

    if purchase_possibility:
        print(f"Для покупки {goods} вам не нужно собирать дополнительные средства. Поздравляем!")
    else:
        print(f"Для покупки {goods} вам нужно еще {price_difference}$.")


def main():
    """
    Основная функция программы.
    """
    name, goods, goods_price, your_money, monthly_deposit = get_user_input()
    purchase_possibility = can_purchase(goods_price, your_money)

    display_results(name, goods, goods_price, your_money, purchase_possibility)
    if not purchase_possibility:
        months_needed = calculate_months_needed(goods_price, your_money, monthly_deposit)
        print(f"Примерное время для накопления средств: {months_needed} месяцев.")


if __name__ == "__main__":
    main()
