class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

def main():
    with open("myfile.txt", "w") as f:
        f.write("Hi there\n")
        f.write("Bye there\n")
        f.close()


    with File("myfile2.txt", "w") as f:
        f.write("Hi there\n")
        f.write("Bye there\n")

if __name__ == '__main__':
    main()
