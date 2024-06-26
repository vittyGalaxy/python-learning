if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(lista)

    lista[0] = 17
    print(lista)

    print(3 in lista)
    print(40 in lista)

    lista2 = (6, 7, 8, 9, 10)
    print(lista2)
    print(6 in lista2)
    print(40 in lista2)

    print(lista[:2])
    print(lista[2:])