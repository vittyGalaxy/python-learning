if __name__ == '__main__':
    print("Hello")

    # assegnazione variabile
    x = "Sera"

    # output
    print("in questo momento e'" + x)

    # input
    x = input("Inserisci numero: ")

    # output
    print(str(x))

    # condition
    if 5 >= int(x) >= 2:
        print("Il numero e' maggiore di 1 e minore di 6")
    else:
        print("Il numero non e' maggiore di 1 e minore di 6")

    a = True
    b = False

    # and
    if a and b:
        print("Entrambi True")
    else:
        print("Uno dei due non e' True")

    # or
    if a or b:
        print("Uno dei 2 e' True")
    else:
        print("Entrambi False")

    # for
    for numero in range(1,10,2):
        print(numero)

    i = 0
    # while
    while i < 8:
        print(i)
        i += 1
