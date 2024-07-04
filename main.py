if __name__ == '__main__':

    f = open("file.txt", "r")
    content = f.read()

    print(content)
    f.close()

    f = open("file.txt", "w")

    f.write("Ciao")

    f.close()

    f = open("file.txt", "r")
    content = f.read()

    print(content)
    f.close()

    with open("file.txt") as name_file:
        content = name_file.read()

        print(content)


    with open("file.txt", "a") as name_file:
        name_file.write(" Bene")


    with open("file.txt") as name_file:
        content = name_file.read()

        print(content)