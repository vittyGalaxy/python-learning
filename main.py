class Product:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price

    def show_info(self):
        print(f"marca: {self.brand}, modello: {self.model}, prezzo: {self.price}")

    def prduct_type(self):
        pass


class Computer(Product):
    def __init__(self, brand, size, price, cpu, ram, memory):
        super().__init__(brand, size, price)
        self.cpu = cpu
        self.ram = ram
        self.memory = memory

    def get_cpu(self):
        return self.cpu

    def get_ram(self):
        return self.ram

    def get_memory(self):
        return self.memory

    def show_info(self):
        super().show_info()
        print(f"cpu: {self.cpu}, ram: {self.ram}, memoria: {self.memory}")

    def prduct_type(self):
        return "Computer"


class Telephone(Product):
    def __init__(self, brand, model, price, screen, battery):
        super().__init__(brand, model, price)
        self.screen = screen
        self.battery = battery

    def get_screen(self):
        return self.screen

    def get_battery(self):
        return self.battery

    def show_info(self):
        super().show_info()
        print(f"schermo: {self.screen}, batteria: {self.battery}")

    def prduct_type(self):
        return "Telefono"


class Tablet(Product):
    def __init__(self, brand, model, price, screen, memory):
        super().__init__(brand, model, price)
        self.screen = screen
        self.memory = memory

    def get_screen(self):
        return self.screen

    def get_memory(self):
        return self.memory

    def show_info(self):
        super().show_info()
        print(f"schermo: {self.screen}, memoria: {self.memory}")

    def prduct_type(self):
        return "Tablet"


def main():
    c1 = Computer("Dell", "XPS 13", 1200.00, "Intel i7", 16, 512)
    c2 = Computer("Apple", "MacBook Pro", 2000.00, "Apple M1", 16, 1024)

    t1 = Telephone("Samsung", "Galaxy S21", 800.00, 6.2, 4000)
    t2 = Telephone("Apple", "iPhone 13", 900.00, 6.1, 3500)

    t3 = Tablet("Apple", "iPad Pro", 1100.00, 11.0, 128)
    t4 = Tablet("Samsung", "Galaxy Tab S7", 650.00, 11.0, 256)

    computer = [c1, c2]
    for c in computer:
        c.show_info()
        print(c.get_brand())
        print(c.get_model())
        print(c.get_price())
        print(c.get_cpu())
        print(c.get_ram())
        print(c.get_memory())
        print(c.prduct_type())

    telephone = [t1, t2]
    for t in telephone:
        t.show_info()
        print(t.get_brand())
        print(t.get_model())
        print(t.get_price())
        print(t.get_screen())
        print(t.get_battery())
        print(t.prduct_type())

    tablet = [t3, t4]
    for t in tablet:
        t.show_info()
        print(t.get_brand())
        print(t.get_model())
        print(t.get_price())
        print(t.get_screen())
        print(t.get_memory())
        print(t.prduct_type())


if __name__ == '__main__':
    main()
