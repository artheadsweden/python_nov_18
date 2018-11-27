class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, a, b):
        return self.x + self.y + a + b

def main():
    m = MyClass(10, 20)
    result = m(5, 6)
    print(result)


if __name__ == '__main__':
    main()
