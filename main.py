class GeometricFigure:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Rectangle(GeometricFigure):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height



def main():
    f = GeometricFigure("Rettangolo")
    print(f.getName())
    r = Rectangle("Rettangolo", 5, 3)
    print(r.getName())
    print(f"Area: {r.area()}")



if __name__ == '__main__':
    main()