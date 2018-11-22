def main():
    with open("mytext.txt", "r") as f:
        for line in f:
            print(line, end="")

    print()

    with open("mytext.txt", "r") as f:
        line = f.readline()
        print(line, end="")

    print()

    with open("mytext.txt", "r") as f:
        line = f.read(3)
        print(line, end="")
        line = f.read(3)
        print(line, end="")

    print()

    with open("mytext.txt", "r") as f:
        lines = f.readlines()
        print(lines)





if __name__ == '__main__':
    main()
