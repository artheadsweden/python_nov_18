from threading import Thread, current_thread
from queue import Queue
import time

def main():
    strings = ["First", "Second", "Third"]
    q = Queue()
    for string in strings:
        q.put(string)

    def worker():
        while not q.empty():
            text = q.get()
            print(current_thread().name, text)
            time.sleep(1)
            q.task_done()

    t1 = Thread(target=worker)
    t1.start()
    t2 = Thread(target=worker)
    t2.start()
    print("Waiting")
    q.join()
    print("Done")


if __name__ == '__main__':
    main()
