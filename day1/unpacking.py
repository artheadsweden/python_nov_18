def main():
    values = (1, 2, 3, 4, 5)
    a, *b, c = values
    print(a, b, c)

    values = [1, 2, 3, 4, 5]
    first, *rest, last = values
    print(first, rest, last)

    first, second,  *_, last = values


if __name__ == '__main__':
    main()
