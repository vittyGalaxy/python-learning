if __name__ == '__main__':
    lista = [["Hello", 33], ["Word", 3]]
    print(lista)

    lista1 = ["Hello", "Word"]
    lista2 = [33, 3]
    unione = zip(lista1, lista2)

    print(list(unione))

    unione = lista1 + lista2
    print(unione)

    lista = range(10)
    print(lista)

    lista = range(10)
    print(list(lista))

    lista = range(2, 10)
    print(list(lista))

    lista = range(2, 10, 3)
    print(list(lista))