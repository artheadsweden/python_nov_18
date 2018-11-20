def func(n):
    return n**2

def main():
    numbers = [1, 2, 3, 4]

    result = list(map(lambda n: n**2, numbers))
    print(result)

if __name__ == '__main__':
    main()
