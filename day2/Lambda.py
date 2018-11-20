def func(x, y):
    return x + y


def runner(f):
    print(f(2, 3))


def main():
    runner(lambda x, y: x if x < y else y)

    f = lambda x, f: f(x*2)
    r = f(10,lambda y: 2 * y)
    print(r)
    ff = lambda x: lambda y: y**x

    s = ff(2)
    c = ff(3)

    print(s(3))
    print(s(4))

    print(c(3))
    print(c(4))



if __name__ == '__main__':
    main()
