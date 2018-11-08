def main():
    a = 10
    b = 10
    c = 11

    print("a =", id(a))
    print("b =", id(b))
    print("c =", id(c))
    a += 1
    print("a =", id(a))
    print("b =", id(b))
    print("c =", id(c))

if __name__ == '__main__':
    main()
