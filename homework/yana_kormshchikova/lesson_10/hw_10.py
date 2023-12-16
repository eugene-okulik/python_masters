import statistics

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23,
                25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def hot_days(x):
    if x > 28:
        return True
    return False


high_temp = filter(hot_days, temperatures)

temp = list(filter(lambda x: x > 28, temperatures))

print(f'Max temperature is: {max(temp)}. \n'
      f'Min temperature is: {min(temp)}. \n'
      f'Average temperature is: {int(sum(temp) / len(temp))}')

# alternative
print(statistics.mean(temp))
