class MusicalInstrument:
    def __init__(self, brand, model, year_of_manufacture):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year_of_manufacture(self):
        return self.year_of_manufacture

    def show_info(self):
        print(f"marca: {self.brand}, modello: {self.model}, anno di fabbricazione: {self.year_of_manufacture}")


class StringInstrument(MusicalInstrument):
    def __init__(self,  brand, model, year_of_manufacture, string_number):
        super().__init__(brand, model, year_of_manufacture)
        self.string_number = string_number

    def get_string_number(self):
        return self.string_number

    def show_info(self):
        super().show_info()
        print(f"numero corde: {self.string_number}")


class WindInstrument(MusicalInstrument):
    def __init__(self, brand, model, year_of_manufacture, material):
        super().__init__(brand, model, year_of_manufacture)
        self.material = material

    def get_material(self):
        return self.material

    def show_info(self):
        super().show_info()
        print(f"materiale: {self.material}")


def main():
    s = StringInstrument("Chitarra", "Fender", 2019, 6)
    w = WindInstrument("Flauto", "Yamaha", 2020, "Legno")

    s.show_info()
    print()
    w.show_info()
    print()

    print(s.get_brand())
    print(s.get_model())
    print(s.get_year_of_manufacture())
    print(s.get_string_number())

    print(w.get_brand())
    print(w.get_model())
    print(w.get_year_of_manufacture())
    print(w.get_material())


if __name__ == '__main__':
    main()
