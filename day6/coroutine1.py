def coroutine():
    print("starting up")
    count = 0
    while True:
        data = yield
        print(data, count)
        count += 1

def main():
    co = coroutine()
    next(co)
    print("Back in main")
    co.send("Hi coroutine")
    print("Back in main")
    co.send("Bye coroutine")

if __name__ == '__main__':
    main()
