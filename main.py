if __name__ == '__main__':

    a = input("Inserisci cosa vuoi mettere nel file: ")
    with open("file_copia.txt", "w") as b:
        b = b.write(a)

    with open("file_copia.txt") as content:
        content = content.read()


    with open("file_copia.txt", "w") as test:
        test.write(content)

    with open("file_copia.txt") as a:
        print(a.read())