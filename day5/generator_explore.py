def my_gen():
    print("Before")
    yield 1
    print("After")


def main():
    g = my_gen()
    print(next(g))
    try:
        next(g)
    except StopIteration as e:
        print("We are done")


if __name__ == '__main__':
    main()
