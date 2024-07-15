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
        print(f"brand: {self.brand}, modello: {self.model}, anno: {self.year}")


class Car(Vehicle):
    def __init__(self,  brand, model, year, number_of_doors):
        super().__init__( brand, model, year)
        self.number_of_doors = number_of_doors

    def get_number_of_doors(self):
        return self.number_of_doors

    def show_info(self):
        super().show_info()
        print(f"numero porte: {self.number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, type_of_motorcycle):
        super().__init__(brand, model, year)
        self.type_of_motocycle = type_of_motorcycle

    def get_type_of_motocycle(self):
        return self.type_of_motocycle

    def show_info(self):
        super().show_info()
        print(f"tipo di moto: {self.type_of_motocycle}")


def main():
    c = Car("Fiat", "Panda", 2015, 5)
    m = Motorcycle("Yamaha", "MT-07", 2018, "Sportiva")
    c.show_info()
    print()
    m.show_info()
    print()

    print(c.get_brand())
    print(c.get_model())
    print(c.get_year())
    print(c.get_number_of_doors())
    print(m.get_brand())
    print(m.get_model())
    print(m.get_year())
    print(m.get_type_of_motocycle())


if __name__ == '__main__':
    main()
