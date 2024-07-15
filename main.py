class ElectricVehicle:
    def __init__(self, brand, model, battery_capacity, autonomy):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.autonomy = autonomy

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_battery_capacity(self):
        return self.battery_capacity

    def get_autonomy(self):
        return self.autonomy

    def show_info(self):
        print(f"marca: {self.brand}, modello: {self.model}, capacita batteria: {self.battery_capacity}, autonomia: {self.autonomy}")


class ElectricCar(ElectricVehicle):
    def __init__(self, brand, model, battery_capacity, autonomy,number_of_seats):
        super().__init__(brand, model, battery_capacity, autonomy)
        self.number_of_seats = number_of_seats

    def get_number_of_seats(self):
        return self.number_of_seats

    def show_info(self):
        super().show_info()
        print(f"numero posti: {self.number_of_seats}")


class ElectricScooter(ElectricVehicle):
    def __init__(self, brand, model, battery_capacity, autonomy, weight):
        super().__init__(brand, model, battery_capacity, autonomy)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def show_info(self):
        super().show_info()
        print(f"peso: {self.weight} kg")


def main():
    c = ElectricCar("Tesla", "Model 3", 75, 400, 5)
    s = ElectricScooter("Xiaomi", "Mi Scooter", 0.5, 30, 12)

    c.show_info()
    print()
    s.show_info()
    print()

    print(c.get_brand())
    print(c.get_model())
    print(c.get_number_of_seats())
    print(c.get_battery_capacity())
    print(c.get_autonomy())

    print(s.get_brand())
    print(s.get_model())
    print(s.get_battery_capacity())
    print(s.get_weight())
    print(s.get_autonomy())


if __name__ == '__main__':
    main()
