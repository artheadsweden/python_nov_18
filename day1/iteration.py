def main():
    for i in range(10): # for(int i = 0; i < 10; i++)
        print(i)

    for i in [2,5,7]:
        print(i)


    for c in "Hi there":
        print(c)

    my_dict = {"name": "Anna", "age": 34, "city": "London"}

    for k, v in my_dict.items():
        print(k, v)

    list_of_values = [2, 5, 4, 7, 4, 87, 98]

    for i in list_of_values:
        print(i)
        if i == 3:
            print("Found 3")
            break
    else:
        print("Did not find 3")

    x = 10
    while x >= 0:
        print(x)
        x -= 1


    while True:
        x += 1
        if x == 7:
            break



if __name__ == '__main__':
    main()
