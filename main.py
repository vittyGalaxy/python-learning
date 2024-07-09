class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * self.radius * 3.14

    def __str__(self):
        return "La circonferenza e' " + str(Circle.circumference(self)) + " e l'area e' " + str(Circle.area(self))

if __name__ == '__main__':
    r = Circle(5.0)
    print(Circle(5.0))
    print(r.getRadius())