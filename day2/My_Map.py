def func(n):
    return n*2

def my_map(f, seq):
    return [f(item) for item in seq]

def main():
    numbers = [1, 2, 3, 4]
    result = list(map(func, numbers))
    print(result)

    result = [func(item) for item in numbers]
    print(result)


if __name__ == '__main__':
    main()
