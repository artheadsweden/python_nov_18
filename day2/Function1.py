def my_func(a, b, c, d=6):
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)
    return a + b + c


def add_name(name, my_list=None):
    if not my_list:
        my_list = []
    my_list.append(name)
    return my_list


def main():
    # result  = my_func(1, 2, 3, 4)
    # result = my_func(b=3, c=2, a=1)
    #print(result)
    result = add_name("John")
    print(result)
    result = add_name("Anna")
    print(result)


if __name__ == '__main__':
    main()
