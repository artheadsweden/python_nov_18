def outer(f):
    def inner():
        result = f()
        return "<<< " + result + " >>>"
    return inner


def my_func():
    return "This is some text"


def main():
    global my_func
    my_func = outer(my_func)

    print(my_func())


if __name__ == '__main__':
    main()
