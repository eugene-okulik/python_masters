def finished_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result

    return wrapper


@finished_decorator
def hello(name: str):
    print(f"Hello {name}")


hello("Dimache")
