def fibonacci_generator(n):
    num_1, num_2 = 0, 1
    for _ in range(n):
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


counter = 1
required_index = [5, 200, 1000, 10000]
req = required_index[0]

for i in fibonacci_generator(150000):

    if counter == req:
        print(f'Number {req} in the list of Fibonacci numbers is {i}')

        required_index.pop(0)
        if len(required_index) > 0:
            req = required_index[0]
        else:
            break
    counter += 1
