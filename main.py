if __name__ == '__main__':
    def divide(a, b):
        try:
            t = a / b
            print(t)

        except:
            print("Attenzione e' successo un casino!")

    divide(3,6)
    divide(8,0)

    def div(a, b):
        try:
            t = a / b
            print(t)

        except ZeroDivisionError:
            print("Attenzione non si puo' dividere per zero!")

    div(6,3)
    div(4,0)

    def divisione(a, b):
        try:
            t = a / b
            print(t)

        except TypeError:
            print("Attenzione e' successo un casino!")

        finally:
            print("programma terminato")

    divisione(8, 4)
    divisione(5, 0)