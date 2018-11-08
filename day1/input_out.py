def main():
    name = "Anna"
    age = 45
    new_string = "First" + "Second"
    print(new_string)
    new_string = name + str(age)
    print("Your \tname \nis", name, "and you are", age, "year old", sep="-")
    print("Second line", end=";")
    print("Third line")

    name = input("Enter your name: ")
    print("Hi", name)

if __name__ == '__main__':
    main()
