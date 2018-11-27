from functools import wraps

def tagit(pre_tag, post_tag):
    def dec_func(f):
        @wraps(f)
        def wrapper(greet, name):
            return pre_tag + f(greet, name) + post_tag
        return wrapper
    return dec_func


@tagit("<h1>","</h1>")
def my_func(greeting, name):
    return name + " says " + greeting


@tagit("<div>","</div>")
def my_func2(greeting, name):
    return name + " says " + greeting


def main():
    print(my_func("Hi", "John"))
    print(my_func2("Yo", "Sara"))


if __name__ == '__main__':
    main()
