def main():
    with open("mytext.txt", "w") as f:
        f.write("Hi there\n")


    with open("mytext.txt", "a") as f:
        f.write("Hi there again\n")


if __name__ == '__main__':
    main()
