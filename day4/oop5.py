class Person:
    pass

def main():
    p1 = Person()
    p2 = Person()
    p1.name = "Bob"
    p2.age = 32
    print(p1.__dict__)
    print(p2.__dict__)


if __name__ == '__main__':
    main()
