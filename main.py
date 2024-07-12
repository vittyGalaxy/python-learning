class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def show_info(self):
        print(f"Marca: {self.brand}, modello: {self.model}")


class Laptop(Computer):
    def __init__(self, brand, model, weight):
        super().__init__(brand, model)
        self.weight = weight

    def get_weight(self):
        return self.weight

    def show_info(self):
        super().show_info()
        print(f"Peso: {self.weight}")


class Desktop(Computer):
    def __init__(self, brand, model, tipo_case):
        super().__init__(brand, model)
        self.tipo_case = tipo_case

    def get_tipo_case(self):
        return self.tipo_case

    def show_info(self):
        super().show_info()
        print(f"Tipo di case: {self.tipo_case}")


def main():
    l = Laptop("Dell", "XPS 13", 1.2)
    d = Desktop("HP", "Omen 30L", "Tower")
    l.show_info()
    print()
    d.show_info()

    print()
    print(l.get_brand())
    print(l.get_model())
    print(l.get_weight())
    print(d.get_brand())
    print(d.get_model())
    print(d.get_tipo_case())


if __name__ == '__main__':
    main()
