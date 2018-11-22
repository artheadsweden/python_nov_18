from functools import wraps

def outer(f):
    @wraps(f)
    def inner():
        result = f()
        return "<<< " + result + " >>>"
    return inner

@outer
def my_func():
    return "This is some text"


def main():
    print(my_func.__name__)
    print(my_func())


if __name__ == '__main__':
    main()
