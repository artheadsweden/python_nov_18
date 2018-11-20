def main():
    numbers1 = [1, 2, 3, 4]
    numbers2 = [5, 6, 7, 8]

    result = [i + j for i in numbers1 for j in numbers2]
    print(result)

    result = []
    for i in numbers1:
        for j in numbers2:
            result.append(i + j)


if __name__ == '__main__':
    main()
