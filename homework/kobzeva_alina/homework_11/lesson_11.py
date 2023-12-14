def finish_me(func):
    def wrapper(*args):
        func(*args)
        print("finished\n")

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
