def main():
    numbers = [1, 2, 3, 4, 5]
    gen = (value**2 for value in numbers)
    for n in gen:
        if n == 9:
            break
        print(n)

    square_values = list(gen)
    print(square_values)


if __name__ == '__main__':
    main()
