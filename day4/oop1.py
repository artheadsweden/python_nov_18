class Person:
    count = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Person.count += 1

    def __str__(self):
        return f"{self.name} has email address {self.email}"

    def __repr__(self):
        return f'Person("{self.name}", "{self.email}")'

    def change_name(self, new_name):
        self.name = new_name

def main():
    p1 = Person("Anna", "anna@email.com")
    p2 = Person("Bob", "bob@email.com")

    p1.change_name("John")
    print(Person.count)
    print(p1.count)
    print(repr(p2))

if __name__ == '__main__':
    main()
