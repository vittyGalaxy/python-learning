class MeansOfTransport:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def show_info(self):
        print(f"Marca: {self.brand}, modello: {self.model}")


class Bicycle(MeansOfTransport):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def get_type_of_bike(self):
        return self.type_of_bike

    def show_info(self):
        super().show_info()
        print(f"tipo di bici: {self.type_of_bike}")


class Car(MeansOfTransport):
    def __init__(self, brand, model, type_of_fuel):
        super().__init__(brand, model)
        self.type_of_fuel = type_of_fuel

    def get_type_of_fuel(self):
        return self.type_of_fuel

    def show_info(self):
        super().show_info()
        print(f"Tipo di carburante: {self.type_of_fuel}")


def main():
    b = Bicycle("Giant", "Defy 3", "Bici da corsa")
    c = Car("Fiat", "Panda", "Benzina")
    b.show_info()
    print()
    c.show_info()

    print(b.get_brand())
    print(b.get_model())
    print(b.get_type_of_bike())
    print(c.get_brand())
    print(c.get_model())
    print(c.get_type_of_fuel())


if __name__ == '__main__':
    main()
