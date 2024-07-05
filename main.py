class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Crea un cerchio con diametro {d}".format(d = diameter))
        self.radius = diameter / 2

    def circumference(self):
        return 2 * self.pi * self.radius

if __name__ == '__main__':
    round_table = Circle(50)
    print(round_table.circumference())
