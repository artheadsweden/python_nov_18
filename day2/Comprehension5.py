def main():
    in_str1 = "John"
    in_str2 = "Anna"
    in_str3 = "Sue"
    s = in_str1 + in_str2 + in_str3
    print(s)

    s = ''.join([in_str1, in_str2, in_str3])
    print(s)

    doc = "Hi there everyone. I am glad to be here! Are you happy?"
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    print(normalized_doc)

if __name__ == '__main__':
    main()
