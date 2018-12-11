def coroutine():
    data = yield "Hello"
    yield data


def coroutine2():
    data = "Empty"
    while True:
        data += yield data

def main():
    co = coroutine2()
    print(next(co))
    print(co.send("World"))
    print(co.send("Oh"))
    print(co.send("Yeah"))


if __name__ == '__main__':
    main()
