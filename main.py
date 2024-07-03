if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    moltiplicatore = 1

    for i in lista:
        moltiplicatore *= i

    print("Il prodotto e': " + str(moltiplicatore))