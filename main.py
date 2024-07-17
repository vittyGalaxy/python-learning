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
    def __init__(self, brand, model, year, number_of_seats, type_of_fuel):
        super().__init__(brand, model, year)
        self.number_of_seats = number_of_seats
        self.type_of_fuel = type_of_fuel

    def get_number_of_seats(self):
        return self.number_of_seats

    def get_type_of_fuel(self):
        return self.type_of_fuel

    def show_info(self):
        super().show_info()
        print(f"numero posti: {self.number_of_seats}, tipo di carburante: {self.type_of_fuel}")


class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity, number_axles):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity
        self.number_axles = number_axles

    def get_load_capacity(self):
        return self.load_capacity

    def get_number_axles(self):
        return self.number_axles

    def show_info(self):
        super().show_info()
        print(f"capacita' carico: {self.load_capacity}, numero assi: {self.number_axles}")


def main():
    c1 = Car("Fiat", "Panda", 2020, 5, "benzina")
    c2 = Car("Tesla", "Model 3", 2021, 5, "elettrico")
    t1 = Truck("Scania", "R450", 2019, 18.0, 4)
    t2 = Truck("Volvo", "FH16", 2022, 25.0, 3)

    c1.show_info()
    print()
    c2.show_info()
    print()
    t1.show_info()
    print()
    t2.show_info()
    print()

    print(c1.get_brand())
    print(c1.get_model())
    print(c1.get_year())
    print(c1.get_number_of_seats())
    print(c1.get_type_of_fuel())

    print(c2.get_brand())
    print(c2.get_model())
    print(c2.get_year())
    print(c2.get_number_of_seats())
    print(c2.get_type_of_fuel())

    print(t1.get_brand())
    print(t1.get_model())
    print(t1.get_year())
    print(t1.get_load_capacity())
    print(t1.get_number_axles())

    print(t2.get_brand())
    print(t2.get_model())
    print(t2.get_year())
    print(t2.get_load_capacity())
    print(t2.get_number_axles())


if __name__ == '__main__':
    main()
