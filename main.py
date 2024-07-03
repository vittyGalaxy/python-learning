if __name__ == '__main__':
    def numero_contenuto(lista):
        l = 0
        lis = []
        for i in lista:
            for k in i:
                l += 1

            lis.append(l)
            l = 0

        return lis

    print(numero_contenuto(["Hello", "World"]))