if __name__ == '__main__':
    a = input("Inserisci un numero: ")
    b = input("Inserisci un numero: ")

    if a > b:
        print("Il maggiore e': " + str(a))
    elif a < b:
        print("Il maggiore e': " + str(b))
    else:
        print("I numeri sono uguali: " + str(a))