if __name__ == '__main__':

    lista = [8, 89, 34, 7, 29]
    l = []

    t = len(lista)

    print(lista)
    print(l)

    while len(l) != t:
        num = lista.pop()
        l.append(num)

    print(lista)
    print(l)

    i = 0

    while i < 10:
        print(i)
        i += 1