class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def show_info(self):
        print(f"Nome: {self.name}, eta': {self.age}")


class Dog(Animal):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def get_race(self):
        return self.race

    def show_info(self):
        super().show_info()
        print(f"Razza: {self.race}")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return self.color

    def show_info(self):
        super().show_info()
        print(f"Colore: {self.color}")


def main():
    d1 = Dog("Fido", 3, "Labrador")
    d2 = Dog("Rex", 5, "Pastore Tedesco")
    c1 = Cat("Micia", 2, "Bianco")
    c2 = Cat("Luna", 4, "Nero")
    d1.show_info()
    print()
    d2.show_info()
    print()
    c1.show_info()
    print()
    c2.show_info()

    print(d1.get_name())
    print(d1.get_age())
    print(d1.get_race())
    print(d2.get_name())
    print(d2.get_age())
    print(d2.get_race())
    print(c1.get_name())
    print(c1.get_age())
    print(c1.get_color())
    print(c1.get_name())
    print(c1.get_age())
    print(c1.get_color())


if __name__ == '__main__':
    main()
