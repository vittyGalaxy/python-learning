if __name__ == '__main__':

    lista = [[12, 34, 34], [2, 5, 67], [2, 4]]
    total = 0

    for i in lista:
        for e in i:
            total += e

    print(total)