def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

def main():
    my_func(1, 2, 3, "hey", name="John", age=13)

    a, *b, c = [1, 2, 3, 4]


if __name__ == '__main__':
    main()
