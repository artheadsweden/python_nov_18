import asyncio
import random

async def my_coroutine(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print(f"Coroutine {id} has successfully completed after {process_time} seconds")

async def async_manager():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(my_coroutine(i)))

    await asyncio.gather(*tasks)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_manager())
    loop.close()


if __name__ == '__main__':
    main()
