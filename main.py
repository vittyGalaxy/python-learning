class HouseholdAppliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def show_info(self):
        print(f"Marca: {self.brand}, Modello: {self.model}")


class Refrigerator(HouseholdAppliance):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def show_info(self):
        super().show_info()
        print(f"Capacita': {self.capacity} litri")


class WashingMachine(HouseholdAppliance):
    def __init__(self, brand, model, weight):
        super().__init__(brand, model)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def show_info(self):
        super().show_info()
        print(f"Carico: {self.weight} kg")


def main():
    f = Refrigerator("Samsung", "RT38K5982SL", 384)
    w = WashingMachine("LG", "F4WV910P2", 10.5)
    f.show_info()
    print()
    w.show_info()
    print(f.get_brand())
    print(f.get_model())
    print(f.get_capacity())
    print(w.get_brand())
    print(w.get_model())
    print(w.get_weight())


if __name__ == '__main__':
    main()
