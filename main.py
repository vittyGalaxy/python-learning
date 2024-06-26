if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]

    print(lista)

    print(len(lista))

    lista.append(6)

    print(lista)

    lista.insert(0,0)
    print(lista)

    print(lista.index(4))

    lista.pop()
    print(lista)

    lista = [4, 3, 2, 1]
    print(lista)

    lista.sort()
    print(lista)

    lista.reverse()
    print(lista)

    lista.remove(3)
    print(lista)

    del lista[0:2]
    print(lista)

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lista)

    del lista[0:4]
    print(lista)

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lista)

    del lista[0:4]
    print(lista)

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    del lista[2:4]
    print(lista)

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    del lista[:4]
    print(lista)

    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    del lista[4:]
    print(lista)