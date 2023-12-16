# Map, filter
# Есть такой список:

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.

# TODO: variant with another list and I didn't get why it works only if
#  I add "list" in from of "hot_days_map1"!!! Otherwise will be an error even if I don't use it!!!

higher_temps = []


def high_temp(x):
    if x > 28:
        higher_temps.append(x)
    return x


hot_days_maped = list(map(high_temp, temperatures))

print(f"Map new list: {higher_temps}")
# print(f"Map original list:", hot_days_maped)

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
print(f"New list elements: Min: {min(higher_temps)}, Max:{max(higher_temps)}, "
      f"Avg:{round((sum(higher_temps) / len(higher_temps)), 2)}\n")


# TODO: variant without another list
def higher_temp(x):
    if x > 28:
        return x
    else:
        return "a"


hot_days = list(map(int, (" ".join(map(str, (list(map(higher_temp, temperatures))))).
                          replace("a", "")).split()))
print("Hot days mapping:", hot_days)

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
print(f"Hot days stats: Min: {min(hot_days)}, Max:{max(hot_days)}, Avg:{round((sum(hot_days) / len(hot_days)), 2)}\n")

# TODO: variant using Filter
hot_days_filter = list(filter(lambda x: True if x > 28 else False, temperatures))
print("Filtered:", *hot_days_filter)

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
print(f"Filtered elements: Min: {min(hot_days_filter)}, Max:{max(hot_days_filter)}, "
      f"Avg:{round((sum(hot_days_filter) / len(hot_days_filter)), 2)}")
