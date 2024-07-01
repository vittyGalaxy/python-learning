if __name__ == '__main__':
    lista = ["Vittorio", "Angelo", "Marco"]

    for nomi in lista:
        print("Benvenuto/a!")

    for i in range(3):
        print("Benvenuto/a!")

    for nomi in lista:
        print(nomi)

    for nomi in lista:
        print(nomi)
        if nomi == "Angelo":
            break

    print("Programma terminato")

    lista = [23, 34, 12, 19, 16]

    for eta in lista:
        if eta < 18:
            continue

        print(eta)