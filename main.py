if __name__ == '__main__':
    def operare(add1, add2):
        sum = add1 + add2
        sub = add1 - add2
        mul = add1 * add2
        div = add1 / add2
        return sum, sub, mul, div

    somma, sottrazione, moltiplicazione, divisione = operare(4, 4)

    print("somma: " + str(somma))
    print("sottrazione: " + str(sottrazione))
    print("moltiplicazione: " + str(moltiplicazione))
    print("divisione: " + str(divisione))

    a = 5
    def operazione(add1, add2 = a):
        sum = add1 + add2
        sub = add1 - add2
        mul = add1 * add2
        div = add1 / add2
        return sum, sub, mul, div

    somma, sottrazione, moltiplicazione, divisione = operazione(4)

    print("somma: " + str(somma))
    print("sottrazione: " + str(sottrazione))
    print("moltiplicazione: " + str(moltiplicazione))
    print("divisione: " + str(divisione))
