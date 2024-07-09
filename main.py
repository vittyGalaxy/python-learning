import math

class Triangle:
    def __init__(self, a, b, c):
        if not (a + b > c) and (a + c > b) and (b + c > a):
            raise ValueError("I lati non possono formare un triangolo")

        self.a = a
        self.b = b
        self.c = c


    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return "Il perimetro e' " + str(Triangle.perimeter(self)) + " e l'area e' " + str(Triangle.area(self))

if __name__ == '__main__':
    t = Triangle(6.0, 8.0, 10.0)
    print(Triangle(6.0, 8.0, 10.0))
    print(t.getA())
    print(t.getB())
    print(t.getC())