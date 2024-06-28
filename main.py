if __name__ == '__main__':
    def super_potenza(x, y):
        if (x ** y) > 4000:
            return True

        else:
            return False


    def diviso_10(x):
        if (x % 10) == 0:
            return True

        else:
            return False

    def in_mezzo(num, alto, basso):
        if (num > basso) and (num < alto):
            return True

        else:
            return False

    print(super_potenza(30, 5))
    print(diviso_10(20))
    print(in_mezzo(22, 33, 11))

    print(super_potenza(1, 2))
    print(diviso_10(42))
    print(in_mezzo(2000, 1, 10))