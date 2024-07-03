if __name__ == '__main__':
    def lunghezza(lista):
        l = 0
        for i in lista:
            l += 1

        return l

    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lunghezza(lis))