def main():
    with open("image.gif", "rb") as f_in:
        # f.seek(13)
        # for i in range(256):
        #     red = f.read(1)
        #     green = f.read(1)
        #     blue = f.read(1)
        #     print(i, red.hex(), green.hex(), blue.hex())
        with open("image2.gif", "wb") as f_out:
            data = f_in.read(19)
            f_out.write(data)
            f_out.write(bytearray([255, 0, 0]))
            f_in.seek(22)
            data = f_in.read()
            f_out.write(data)


if __name__ == '__main__':
    main()
