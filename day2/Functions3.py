def my_func(a: int, b: int) -> int:
    return a + b


def my_func2(a: int, b: int) -> tuple(int, int, int):
    return a+1, b+2, a+b


def main():
    print(my_func([1,2], [22,34]))

    a, b, c = my_func2(1, 2)
    print(a)

if __name__ == '__main__':
    main()
