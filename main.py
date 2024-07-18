class Form:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def show_info(self):
        print(f"colore: {self.color}")


class Circle(Form):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def show_info(self):
        super().show_info()
        print(f"radius: {self.radius}")

    def make_area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Form):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def get_base(self):
        return self.base

    def get_height(self):
        return self.height

    def show_info(self):
        super().show_info()
        print(f"base: {self.base}, altezza: {self.height}")

    def make_area(self):
        return self.base * self.height


def main():
    c1 = Circle("Rosso", 5)
    c2 = Circle("Blu", 3)

    r1 = Rectangle("Verde", 4, 6)
    r2 = Rectangle("Giallo", 2, 8)

    circle = [c1, c2]
    for c in circle:
        c.show_info()
        print(c.get_color())
        print(c.get_radius())
        print(c.make_area())

    rectangle = [r1, r2]
    for r in rectangle:
        r.show_info()
        print(r.get_color())
        print(r.get_base())
        print(r.get_height())
        print(r.make_area())


if __name__ == '__main__':
    main()
