if __name__ == '__main__':
    def controllo(nome):
        if nome == "Vittorio":
            return "Benvenuto Vittorio!"


    print(controllo("Vittorio"))
    print(controllo("Luca"))


    def maggiore(x, y):
        if x > y:
            return x

        if x < y:
            return y

        if x == y:
            return "I numeri sono uguali"


    print(maggiore(6, 4))
    print(maggiore(3, 4))
    print(maggiore(4, 4))


    def functionAnd(x, y):
        if (x > 3) and (y > 5):
            return True


    print(functionAnd(4, 6))
    print(functionAnd(4, 5))


    def functionOr(x, y):
        if (x > 3) or (y > 5):
            return True


    print(functionOr(4, 5))