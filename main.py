if __name__ == '__main__':
    a = input("Inserisci un numero: ")
    b = input("Inserisci un numero: ")
    c = input("Inserisci un numero: ")

    if a > b:
        mx = a
    else:
        mx = b

    if mx > c:
        print("Il maggiore e': " + str(mx))
    else:
        print("Il maggiore e': " + str(c))