class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def show_info(self):
        print(f"marca: {self.brand}, modello: {self.model}, anno: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, boot_capacity):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.boot_capacity = boot_capacity

    def get_number_of_doors(self):
        return self.number_of_doors

    def get_boot_capacity(self):
        return self.boot_capacity

    def show_info(self):
        super().show_info()
        print(f"numero porte: {self.number_of_doors}, capacita' bagaglio: {self.boot_capacity}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, displacement, typee):
        super().__init__(brand, model, year)
        self.displacement = displacement
        self.typee = typee

    def get_displacement(self):
        return self.displacement

    def get_typee(self):
        return self.typee

    def show_info(self):
        super().show_info()
        print(f"cilindrata: {self.displacement}, tipo: {self.typee}")


def main():
    c1 = Car("Fiat", "500", 2019, 3, 185)
    c2 = Car("Samsung", "Galaxy S23", 3900, 6.8, 256)
    m1 = Motorcycle("Ducati", "Panigale V4", 2021, 1103, "Sport")
    m2 = Motorcycle("Harley-Davidson", "Iron 883", 2018, 883, "Cruiser")

    c1.show_info()
    print()
    c2.show_info()
    print()
    m1.show_info()
    print()
    m2.show_info()
    print()


    print(c1.get_brand())
    print(c1.get_model())
    print(c1.get_year())
    print(c1.get_number_of_doors())
    print(c1.get_boot_capacity())

    print(c2.get_brand())
    print(c2.get_model())
    print(c2.get_year())
    print(c2.get_number_of_doors())
    print(c2.get_boot_capacity())

    print(m1.get_brand())
    print(m1.get_model())
    print(m1.get_year())
    print(m1.get_displacement())
    print(m1.get_typee())

    print(m2.get_brand())
    print(m2.get_model())
    print(m2.get_year())
    print(m2.get_displacement())
    print(m2.get_typee())


if __name__ == '__main__':
    main()
