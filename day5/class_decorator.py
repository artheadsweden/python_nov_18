class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

    def say_hi(self):
        print("hi")


@CallCount
def hello(name):
    print("Hello", name)

def main():
    hello("John")
    hello("Anna")
    hello("Bob")
    print(hello.count)
    hello.say_hi()

    a = CallCount(lambda x: print(x))
    a("Coffee")
    print(a.count)


if __name__ == '__main__':
    main()
