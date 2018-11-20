def square(n):
    return n**2

def main():
    numbers = [1, 2, 3, 4]

    result = [square(value) for value in numbers]

    result = [value**2 for value in numbers if value % 2 == 0]
    print(result)

    result = [value**2 if value % 2 == 0 else value for value in numbers if value < 3]
    print(result)
if __name__ == '__main__':
    main()
