import asyncio
import time
import requests
from threading import Thread
from queue import Queue
from multiprocessing import Pool
import aiohttp

def fetch(url):
    return requests.get(url)


class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start
        print(f"It took {duration:.2f} for {self.name}")


def get_sequential(urls):
    return [fetch(url) for url in urls]


def get_multithreaded(urls):
    q = Queue()
    for url in urls:
        q.put(url)

    results = []

    def worker():
        while not q.empty():
            u = q.get()
            results.append(fetch(u))
            q.task_done()

    threads = [Thread(target=worker) for _ in range(5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return results

def get_multiprocess(urls):
    with Pool(5) as pool:
        results = pool.map(fetch, urls)
    return results

def get_async(urls):
    results = []

    async def get(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                results.append(response)

    loop = asyncio.get_event_loop()

    task = [
        asyncio.ensure_future(get(url))
        for url in urls
    ]
    loop.run_until_complete(asyncio.wait(task))
    loop.close()
    return results


def main():
    urls = [
        "http://dn.se",
        "http://cnn.com",
        "http://bbc.co.uk",
        "http://svt.se"
    ]*30

    #with Timer("Sequential"):
    #    result = get_sequential(urls)

    with Timer("Multi threaded"):
        result = get_multithreaded(urls)

    with Timer("Multi process"):
        result = get_multiprocess(urls)

    with Timer("Async"):
        result = get_async(urls)

if __name__ == '__main__':
    main()
