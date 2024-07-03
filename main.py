if __name__ == '__main__':
    lista = [1, 3, 5, 3, 8, 5, 6]
    mx = lista[0]

    for i in lista:
        if mx < i:
            mx = i

    print("Il maggiore e': " + str(mx))