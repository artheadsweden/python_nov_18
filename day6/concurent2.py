import time
from math import sqrt
from multiprocessing.pool import Pool
from queue import Queue
from threading import Thread


class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start
        print(f"It took {duration:.2f} for {self.name}")



def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    max = int(sqrt(n)) + 1

    for i in range(3, max):
        if n % i == 0:
            return False
    return True

def create_lists(seq, num_subs):
    q, r = divmod(len(seq), num_subs)
    return (seq[i * q + min(i, r):(i + 1) * q + min(i + 1, r)] for i in range(num_subs))


def check_threading(lists):
    q = Queue()
    for l in lists:
        q.put(l)

    results = []

    def worker():
        while not q.empty():
            values = q.get()
            for value in values:
                if is_prime(value):
                    results.append(value)
            q.task_done()

    threads = [Thread(target=worker) for _ in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return results

def process_values(values):
    return [value for value in values if is_prime(value)]

def check_multiprocessing(lists):
    with Pool(5) as pool:
        results = pool.map(process_values, lists)
    results = [item for sublist in results for item in sublist]
    return results

def main():

    #with Timer("Sequential"):
    #    primes = [i for i in range(2_000_000) if is_prime(i)]

    #lists = create_lists(list(range(2_000_000)), 1000)
    #with Timer("Multi Threading"):
    #    primes = check_threading(lists)

    lists = create_lists(list(range(2_000_000)), 1000)
    with Timer("Multi Processing"):
        primes = check_multiprocessing(lists)

if __name__ == '__main__':
    main()
