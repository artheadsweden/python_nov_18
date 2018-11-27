class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.__y = y

    def __str__(self):
        return str(self.x) + " - " + str(self.__y)

def main():
    p1 = MyClass(10, 20)
    p1.name = "Bob"
    p1.__y = 30
    print(p1.__dict__)
    print(p1)


if __name__ == '__main__':
    main()
