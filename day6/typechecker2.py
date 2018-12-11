from functools import wraps
from inspect import signature


def typecheck(f):
    if not __debug__:
        return f
    sig = signature(f)
    bound_types = sig.parameters

    @wraps(f)
    def wrapper(*args, **kwargs):
        bound_values = sig.bind(*args, **kwargs).arguments
        for name, value in bound_values.items():

            if not isinstance(value, bound_types[name].annotation):
                raise TypeError(f"Argument {name} is {type(value)}. Expected {bound_types[name]}.")

        if "return" in f.__annotations__:
            return_value = f(*args, **kwargs)

            if not isinstance(return_value, f.__annotations__["return"]):
                raise TypeError(f"Return value is {type(return_value)}, expected {f.__annotations__['return']}.")
            else:
                return return_value
        else:
            return f(*args, **kwargs)
    return wrapper


@typecheck
def try_me(a: int, b: str, c: float) -> int:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    print(a, b, c)
    return 2


def main():
    try_me(3, "hi", 3.4)


if __name__ == '__main__':
    main()
