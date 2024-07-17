class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_name(self):
        return self.name

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age

    def show_info(self):
        print(f"nome: {self.name}, altezza: {self.height}, eta': {self.age}")


class Tree(Plant):
    def __init__(self, name, height, age, wood_type):
        super().__init__(name, height, age)
        self.wood_type = wood_type

    def get_wood_type(self):
        return self.wood_type

    def show_info(self):
        super().show_info()
        print(f"tipo di legno: {self.wood_type}")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_color(self):
        return self.color

    def show_info(self):
        super().show_info()
        print(f"colore: {self.color}")


def main():
    t1 = Tree("Quercia", 15, 50, "duro")
    t2 = Tree("Pino", 20, 30, "morbido")
    f1 = Flower("Rosa", 0.5, 2, "rosso")
    f2 = Flower("Tulipano", 0.3, 1, "giallo")

    tree = [t1, t2]
    for t in tree:
        t.show_info()
        print(t.get_name())
        print(t.get_height())
        print(t.get_age())
        print(t.get_wood_type())

    flower = [f1, f2]
    for f in flower:
        f.show_info()
        print(f.get_name())
        print(f.get_height())
        print(f.get_age())
        print(f.get_color())


if __name__ == '__main__':
    main()
