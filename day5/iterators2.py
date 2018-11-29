def main():
    my_list = [1, 2, 3, 4]
    for value in my_list:
        print(value)

    print("="*30)

    iter_obj = iter(my_list)
    while True:
        try:
            element = next(iter_obj)
            print(element)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
