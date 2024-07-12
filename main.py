class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def show_info(self):
        print(f"Marca: {self.name}, modello: {self.age}")


class Mammal(Animal):
    def __init__(self, name, age, type_of_fur):
        super().__init__(name, age)
        self.type_of_fur = type_of_fur

    def get_type_of_fur(self):
        return self.type_of_fur

    def show_info(self):
        super().show_info()
        print(f"Tipo di pelliccia: {self.type_of_fur}")


class Bird(Animal):
    def __init__(self, name, age, type_of_beak):
        super().__init__(name, age)
        self.type_of_beak = type_of_beak

    def get_type_of_beak(self):
        return self.type_of_beak

    def show_info(self):
        super().show_info()
        print(f"Tipo di becco: {self.type_of_beak}")


def main():
    m = Mammal("Leone", 7, "Lunga e folta")
    b = Bird("Aquila", 5, "Appuntito")
    m.show_info()
    print()
    b.show_info()

    print()
    print(m.get_name())
    print(m.get_age())
    print(m.get_type_of_fur())
    print(b.get_name())
    print(b.get_age())
    print(b.get_type_of_beak())


if __name__ == '__main__':
    main()
