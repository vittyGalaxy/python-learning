import math

class Form:
    def area(self):
        pass



class Square(Form):
    def __init__(self, base):
        super().__init__()
        self.base = base

    def getBase(self):
        return self.base

    def area(self):
        return self.base ** 2

class Circle(Form):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2



if __name__ == '__main__':
    q = Square(5)
    print(q.getBase())
    print(q.area())
    c = Circle(5)
    print(c.getRadius())
    print(c.area())