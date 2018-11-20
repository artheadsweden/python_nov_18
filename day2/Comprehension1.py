def main():
    numbers = [1, 2, 3, 4]

    result = []
    for value in numbers:
        result.append(value**2)

    print(result)

    result = [value**2 for value in numbers]
    print(result)

if __name__ == '__main__':
    main()
