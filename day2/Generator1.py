def my_range(n):
    result = []
    i = 0
    while i < n:
        result.append(i)
        i += 1
    return result


def my_gen(n):
    i = 0
    while i < n:
        yield i
        i += 1

def main():

    for i in my_gen(10):
        print(i)


    #for i in my_range(10000000):
    #    print(i)


if __name__ == '__main__':
    main()
