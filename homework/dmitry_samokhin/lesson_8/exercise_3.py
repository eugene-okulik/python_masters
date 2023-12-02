def addition_10(*args: str):
    for val in args:
        print(int(val[val.index(":") + 2:]) + 10)


addition_10(
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
)
