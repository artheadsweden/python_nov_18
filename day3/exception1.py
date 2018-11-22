def my_func(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        raise ValueError("Argument b can't be 0")
    return result

def main():
    try:
        result = my_func(10, 0)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(result)
    finally:
        print("We will always do this")

    print("We are done")


if __name__ == '__main__':
    main()
