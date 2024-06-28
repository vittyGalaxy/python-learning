if __name__ == '__main__':
    def convertitore(voto):
        if voto >= 9.0:
            return "A"

        elif voto >= 7.0:
            return "B"

        elif voto >= 6.0:
            return "C"

        elif voto >= 5.0:
            return "D"

        else:
            return "F"

    print(convertitore(9))
    print(convertitore(7))
    print(convertitore(6))
    print(convertitore(5))
    print(convertitore(2))