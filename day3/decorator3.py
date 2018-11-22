import time
from functools import wraps


def cache(f):
    the_cache = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        kwarg_vals = tuple([(k, v) for k, v in kwargs.items()])
        key = (args, kwarg_vals)
        if key in the_cache:
            return the_cache[key]
        return_value = f(*args, **kwargs)
        the_cache[key] = return_value
        return return_value
    return wrapper


@cache
def my_calc_func(a, b):
    time.sleep(2)
    return a+b

@cache
def my_func(a, b, c = 10):
    return a + b + c

def main():
    print(my_func(12, 13, c = 34))
    print(my_func(12, 13, c = 34))
    # start = time.time()
    # print(my_calc_func(1, 2))
    # end = time.time()
    # print("It took", end - start, "seconds")
    #
    # start = time.time()
    # print(my_calc_func(1, 2))
    # end = time.time()
    # print("It took", end - start, "seconds")


if __name__ == '__main__':
    main()
