class Square:
    def __init__(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def area(self):
        return self.base * self.getBase()

    def perimeter(self):
        return self.base * 4

    def __str__(self):
        return "Il perimetro e' " + str(Square.perimeter(self)) + " e l'area e' " + str(Square.area(self))

if __name__ == '__main__':
    s = Square(5.0)
    print(Square(5.0))
    print(s.getBase())