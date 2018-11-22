import time


def my_calc_func(a, b, cache = {}):
    key = (a, b)
    if key in cache:
        return cache[key]
    result = a + b
    cache[key] = result
    time.sleep(2)
    return result

def main():
    start = time.time()
    print(my_calc_func(1, 2))
    end = time.time()
    print("It took", end - start, "seconds")

    start = time.time()
    print(my_calc_func(1, 2))
    end = time.time()
    print("It took", end - start, "seconds")


if __name__ == '__main__':
    main()
