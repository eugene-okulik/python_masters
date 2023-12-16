def finish_func(func):

    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper


@finish_func
def calc(num1, num2):
    print(num2 + num1)


@finish_func
def print_text(text):
    print(text)


calc(2, 4)
print_text("that's all")
