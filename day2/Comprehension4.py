def main():
    numbers = [(1, 2, 3), (2, 3, 4), (5, 6, 7)]

    reslut = [[value**2 for value in i] for i in numbers if i[0] > 1]
    print(reslut)

if __name__ == '__main__':
    main()
