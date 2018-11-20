# LEGB

x = 10
y = 99

def my_func():
    #global x
    y = 11
    print(id(y))
    def inner():
        nonlocal y
        print(id(y))
        y += 1
        print(id(y))
        # print(x, y)
    inner()
    print(id(y))


def main():
    my_func()


if __name__ == '__main__':
    main()
