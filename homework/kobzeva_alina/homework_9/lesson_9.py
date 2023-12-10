def fibonacci():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

fib = fibonacci()


for i in range(5):
    next(fib)
fifth = next(fib)

for i in range(195):
    next(fib)
two_hundredth = next(fib)

for i in range(800):
    next(fib)
thousandth = next(fib)

for i in range(99000):
    next(fib)
hundred_thousandth = next(fib)

print("Fifth Fibonacci number:", fifth)
print("Two hundredth Fibonacci number:", two_hundredth)
print("Thousandth Fibonacci number:", thousandth)
print("Hundred thousandth Fibonacci number:", hundred_thousandth)
