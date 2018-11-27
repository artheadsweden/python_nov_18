class A:
    def __init__(self):
        print("A.__init__()")
        self.x = 10

    def printer(self):
        print(self.x)


class B(A):
    def __init__(self):
        super().__init__()
        print("B.__init__()")
        self.x = 20


class C(A):
    def __init__(self):
        super().__init__()
        print("C.__init__()")
        self.x = 30

class D(C, B):
    def __init__(self):
        super().__init__()
        print("D.__init__()")

    def printer(self):
        print("Yay I am D and x is:")
        super().printer()

def main():
    d = D()
    d.printer()


if __name__ == '__main__':
    main()
