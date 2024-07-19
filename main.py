class Vehicle:
    def __init__(self, brand, model, price, consumption):
        self.brand = brand
        self.model = model
        self.price = price
        self.consumption = consumption

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def get_consumption(self):
        return self.consumption

    def show_info(self):
        print(f"marca: {self.brand}, modello: {self.model}, prezzo: {self.price}, consumo: {self.consumption}")

    def calculate_fuel_cost(self, km, fuel_price):
        litres_necessary = (self.consumption / 100) * km
        total_cost = litres_necessary * fuel_price
        return  round(total_cost, 2)


class Car(Vehicle):
    def __init__(self, brand, model, price, consumption, number_of_doors):
        super().__init__(brand, model, price, consumption)
        self.number_of_doors = number_of_doors

    def get_number_of_doors(self):
        return self.number_of_doors

    def show_info(self):
        super().show_info()
        print(f"numero porte: {self.number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, price, consumption, typee):
        super().__init__(brand, model, price, consumption)
        self.typee = typee

    def get_typee(self):
        return self.typee

    def show_info(self):
        super().show_info()
        print(f"tipo: {self.typee}")


class Truck(Vehicle):
    def __init__(self, brand, model, price, consumption, load_capacity):
        super().__init__(brand, model, price, consumption)
        self.load_capacity = load_capacity

    def get_load_capacity(self):
        return self.load_capacity

    def show_info(self):
        super().show_info()
        print(f"capacita' carico: {self.load_capacity}")


def main():
    c1 = Car("Fiat", "Panda", 10000.0, 5.0, 5)
    c2 = Car("Tesla", "Model S", 80000.0, 0.0, 4)

    m1 = Motorcycle("Yamaha", "MT-07", 7000.0, 4.3, "Sportiva")
    m2 = Motorcycle("Harley-Davidson", "Iron 883", 9000.0, 5.6, "Cruiser")

    t1 = Truck("Iveco", "Stralis", 50000.0, 25.0, 18)
    t2 = Truck("Mercedes", "Actros", 60000.0, 30.0, 20)

    km = 150
    fuel_price = 1.5

    car = [c1, c2]
    for c in car:
        c.show_info()
        print(c.get_brand())
        print(c.get_model())
        print(c.get_price())
        print(c.get_consumption())
        print(c.get_number_of_doors())
        print(c.calculate_fuel_cost(km, fuel_price))

    motorcycle = [m1, m2]
    for m in motorcycle:
        m.show_info()
        print(m.get_brand())
        print(m.get_model())
        print(m.get_price())
        print(m.get_consumption())
        print(m.get_typee())
        print(m.calculate_fuel_cost(km, fuel_price))

    truck = [t1, t2]
    for t in truck:
        t.show_info()
        print(t.get_brand())
        print(t.get_model())
        print(t.get_price())
        print(t.get_consumption())
        print(t.get_load_capacity())
        print(t.calculate_fuel_cost(km, fuel_price))


if __name__ == '__main__':
    main()
