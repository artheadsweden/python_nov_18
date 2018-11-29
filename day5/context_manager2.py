from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    # This section is like __enter__
    the_file = open(filename, mode)
    yield the_file

    # This section is like __exit__
    the_file.close()



def main():
    with open_file("myfile3.txt", "w") as f:
        f.write("Hi there\n")
        f.write("Bye there\n")


if __name__ == '__main__':
    main()
