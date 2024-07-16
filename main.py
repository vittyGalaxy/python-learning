class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age

    def show_info(self):
        print(f"nome: {self.name}, specie: {self.species}, eta': {self.age}")


class Mammal(Animal):
    def __init__(self, name, species, age, hair_length, eating_habits):
        super().__init__(name, species, age)
        self.hair_length = hair_length
        self.eating_habits = eating_habits

    def get_hair_lenght(self):
        return self.hair_length

    def get_eatin_habits(self):
        return self.eating_habits

    def show_info(self):
        super().show_info()
        print(f"lunghezza pelo: {self.hair_length}, abitudini alimentari: {self.eating_habits}")


class Bird(Animal):
    def __init__(self, name, species, age, wingspan, migratory):
        super().__init__(name, species, age)
        self.wingspan = wingspan
        self.migratory = migratory

    def get_wingspan(self):
        return self.wingspan

    def get_migratory(self):
        return self.migratory

    def show_info(self):
        super().show_info()
        if self.migratory:
            self.migratory = "Si"

        else:
            self.migratory = "No"
        print(f"apertura alare: {self.wingspan}, migratore: {self.migratory}")


def main():
    m1 = Mammal("Leo", "Leone", 5, 2.5, "carnivoro")
    m2 = Mammal("Ella", "Elefante", 10, 0.5, "erbivoro")
    b1 = Bird("Robin", "Pettirosso", 2, 30.0, True)
    b2 = Bird("Polly", "Pappagallo", 4, 50.0, False)

    m1.show_info()
    print()
    m2.show_info()
    print()
    b1.show_info()
    print()
    b2.show_info()
    print()


    print(m1.get_name())
    print(m1.get_species())
    print(m1.get_age())
    print(m1.get_hair_lenght())
    print(m1.get_eatin_habits())

    print(m2.get_name())
    print(m2.get_species())
    print(m2.get_age())
    print(m2.get_hair_lenght())
    print(m2.get_eatin_habits())

    print(b1.get_name())
    print(b1.get_species())
    print(b1.get_age())
    print(b1.get_wingspan())
    print(b1.get_migratory())

    print(b2.get_name())
    print(b2.get_species())
    print(b2.get_age())
    print(b2.get_wingspan())
    print(b2.get_migratory())


if __name__ == '__main__':
    main()
