import sys

sys.set_int_max_str_digits(100000)


def fibo():
    f1, f2 = 0, 1
    while True:
        yield f2
        f1, f2 = f2, f1 + f2


count = 1
for num in fibo():
    match count:
        case 5:
            print(num)
        case 200:
            print(num)
        case 1000:
            print(num)
        case 100_000:
            print(num)
            break
    count += 1
