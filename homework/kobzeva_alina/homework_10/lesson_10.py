temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
hot_days = list(filter(lambda x: x > 28, temperatures))
hot_temperatures = list(map(lambda x: x, hot_days))

max_temp = max(hot_temperatures)
min_temp = min(hot_temperatures)
average_temp = sum(hot_temperatures) / len(hot_temperatures)

print("Самая высокая температура:", max_temp)
print("Самая низкая температура:", min_temp)
print("Средняя температура:", average_temp)
