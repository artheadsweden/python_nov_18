def main():
    number = 10
    other_number = 11

    if number > 8 and other_number == 11:
        print("This is true")
        print(number, "is greater than 8")
    else:
        print("This is false")
        print(number, "is less or equal to 8")

    print("After if")

    value = 10

    if value < 10:
        print("< 10")
    elif value < 20:
        print("< 20")
    elif value < 30:
        print("< 30")
    else:
        print(">= 30")

if __name__ == '__main__':
    main()
