from functools import wraps
from inspect import signature

def typechecker(*tc_args, **tc_kwargs):
    def decorator(f):
        if not __debug__:
            return f
        sig = signature(f) # get args to decorated function
        bound_types = sig.bind(*tc_args, **tc_kwargs).arguments  # Bind args with types

        @wraps(f)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs).arguments
            for name, value in bound_values.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f"Argument {name} is {type(value)}. Expected {bound_types[name]}.")
            return f(*args, **kwargs)
        return wrapper
    return decorator


@typechecker(int, str, float)
def try_me(a, b, c):
    print(a, b, c)


def main():
    try_me(5, "hi", 5.6)   # Ok
    #try_me(3, "5", 3.4)  # Exception


if __name__ == '__main__':
    main()
