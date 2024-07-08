class Rational:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        r1 = self.number1
        r2 = self.number2
        for i in range(2, self.number1 + 1):
            if ((self.number1 % i) == 0) and ((self.number2 % i) == 0):
                r1 = self.number1 / i
                r2 = self.number2 / i
                i = 2
        print("Razionalizzando e': " + str(r1) + "/" + str(r2))
        return self.number1 / self.number2


if __name__ == '__main__':

    r = Rational(5,10)
    print(r.sum())
    print(r.subtraction())
    print(r.multiplication())
    print(r.division())

    r = Rational(20,40)
    print(r.sum())
    print(r.subtraction())
    print(r.multiplication())
    print(r.division())

    r = Rational(30,46)
    print(r.sum())
    print(r.subtraction())
    print(r.multiplication())
    print(r.division())
