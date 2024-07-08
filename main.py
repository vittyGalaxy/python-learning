class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def getBase(self):
        return self.base

    def getHeight(self):
        return self.height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return (self.base + self.height) * 2

    def __str__(self):
        return "Il perimetro e' " + str(Rectangle.perimeter(self)) + " e l'area e' " + str(Rectangle.area(self))

if __name__ == '__main__':
    r = Rectangle(2, 3)
    print(Rectangle(2, 3))
    print(r.getBase())
    print(r.getHeight())