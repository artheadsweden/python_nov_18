def main():
    i = 10
    i += 1
    print(type(i))
    f = 4.5
    print(type(f))

    i = True
    print(type(i))
    i = "Hi there"
    print("Hi" in i)
    print(type(i))

    i = 10
    j = 10**2
    print(i is j)

    x = -5
    y = 2
    print(x // y)
    print(x / y)

if __name__ == '__main__':
    main()
