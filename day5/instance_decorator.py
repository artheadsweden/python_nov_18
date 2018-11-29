from functools import wraps

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f.__name__}")
            return f(*args, **kwargs)
        return wrapper

tracer = Trace()


@tracer
def list_rotator(list):
    return list[1:] + [list[0]]


def main():
    my_list = [1, 2, 3, 4]
    my_list = list_rotator(my_list)
    print(my_list)
    tracer.enabled = False
    my_list = list_rotator(my_list)
    print(my_list)
    print(list_rotator.__name__)

if __name__ == '__main__':
    main()
