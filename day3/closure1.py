
def outer(x):
    def inner(y):
        return x + y
    return inner


def main():
    a = outer(10)
    result = a(5)
    print(result)


if __name__ == '__main__':
    main()
