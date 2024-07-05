if __name__ == '__main__':

    string = input("Inserisci cosa vuoi mettere nel file: ")
    with open("file.txt","w") as test:
        content = test.write(string)

    with open("file.txt") as test:
        print(test.read())
