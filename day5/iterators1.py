def main():
    my_list = [1, 2, 3, 4]
    my_iter = iter(my_list)

    for value in my_iter:
        print(value)
        if value == 2:
            break

    print("No my_iter is:", next(my_iter))

if __name__ == '__main__':
    main()
