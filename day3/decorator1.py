from functools import wraps

def logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"Call to function {f.__name__}")
        print(f"Positional arguments {args}")
        print(f"Keyword arguments {kwargs}")
        return_value = f(*args, **kwargs)
        print(f"Function returned {return_value}")
        return return_value
    return wrapper

@logger
def my_func(a, b, c = 10):
    return a + b

def main():
    print(my_func(1, 2, c = 13))


if __name__ == '__main__':
    main()
