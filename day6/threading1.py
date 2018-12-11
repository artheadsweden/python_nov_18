from threading import Thread
import time


def worker():
    print("Working")
    time.sleep(2)
    print("Done working")


def main():
    t1 = Thread(target=worker)
    t1.start()
    t2 = Thread(target=worker)
    t2.start()
    print("Waiting for threads")
    t1.join()
    t2.join()
    print("We are done waiting")


if __name__ == '__main__':
    main()
