class Device:
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


class Laptop(Device):
    def __init__(self,  brand, model, year, ram, processor):
        super().__init__( brand, model, year)
        self.ram = ram
        self.processor = processor

    def get_ram(self):
        return self.ram

    def get_processor(self):
        return self.processor

    def show_info(self):
        super().show_info()
        print(f"ram: {self.ram}, processore: {self.processor}")


class Smartphone(Device):
    def __init__(self, brand, model, year, internal_memory, number_of_cameras):
        super().__init__(brand, model, year)
        self.internal_memory = internal_memory
        self.number_of_cameras = number_of_cameras

    def get_internal_memory(self):
        return self.internal_memory

    def get_number_of_cameras(self):
        return self.number_of_cameras

    def show_info(self):
        super().show_info()
        print(f"memoria interna: {self.internal_memory}, numero fotocamere: {self.number_of_cameras}")


def main():
    l = Laptop("Apple", "MacBook Pro", 2021, 16, "M1")
    s = Smartphone("Samsung", "Galaxy S21", 2021, 128, 4)
    l.show_info()
    print()
    s.show_info()
    print()

    print(l.get_brand())
    print(l.get_model())
    print(l.get_year())
    print(l.get_processor())
    print(l.get_ram())

    print(s.get_brand())
    print(s.get_model())
    print(s.get_year())
    print(s.get_internal_memory())
    print(s.get_number_of_cameras())


if __name__ == '__main__':
    main()
