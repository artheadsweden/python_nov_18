from threading import Thread, Lock

def main():
    x = 0
    x_lock = Lock()

    def worker():
        nonlocal x
        for _ in range(1_000_000):
            if x_lock.acquire(blocking=True):
                x += 1
                x_lock.release()
            else:
                print("Something else")

    threads = [Thread(target=worker) for _ in range(4)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(x)


if __name__ == '__main__':
    main()
