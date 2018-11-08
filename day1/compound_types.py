def main():
    numbers = [2, "hi3", True, 5] # List, mutable
    numbers.insert(0, 1)
    print(numbers)

    values = (1, 2, 3)      # Tuple immutable
    print(values)

    list_tuple = ([], [], [])
    list_tuple[0].append(1)
    print(list_tuple[0][0])

    my_set1 = {1, 2, 3, 2}  # Set mutable
    print(my_set1)
    my_set2 = {2, 4, 6}

    my_list = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 6]
    print(set(my_list))

    print(my_set1)
    print(my_set1.intersection(my_set2))


    my_dict = {"name": "Anna", "age": 34}  # dict mutable
    print(my_dict["name"])
    my_dict["city"] = "London"

if __name__ == '__main__':
    main()
