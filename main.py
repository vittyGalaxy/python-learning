class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount

    def show_info(self):
        print(f"nome: {self.name}, prezzo: {self.price}, quantita': {self.amount}")

    def calculate_counted_price(self, discount):
        discounted_price = self.price * (1 - discount / 100)
        return round(discounted_price, 2)


class Computer(Product):
    def __init__(self, name, price, amount, processor, ram):
        super().__init__(name, price, amount)
        self.processor = processor
        self.ram = ram

    def get_ram(self):
        return self.ram

    def get_processor(self):
        return self.processor

    def show_info(self):
        super().show_info()
        print(f"ram: {self.ram}, processore: {self.processor}")


class Telephone(Product):
    def __init__(self, name, price, amount, brand, model):
        super().__init__(name, price, amount)
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def show_info(self):
        super().show_info()
        print(f"marca: {self.brand}, modello: {self.model}")


class Television(Product):
    def __init__(self, name, price, amount, size, resolution):
        super().__init__(name, price, amount)
        self.size = size
        self.resolution = resolution

    def get_size(self):
        return self.size

    def get_resolution(self):
        return self.resolution

    def show_info(self):
        super().show_info()
        print(f"dimensioni: {self.size}, risoluzione: {self.resolution}")


def main():
    c1 = Computer("Laptop HP", 1200.0, 10, "Intel i7", 16)
    c2 = Computer("MacBook Pro", 2500.0, 5, "Apple M1", 16)

    t1 = Telephone("iPhone 13", 999.0, 15, "Apple", "13")
    t2 = Telephone("Samsung Galaxy S21", 799.0, 20, "Samsung", "Galaxy S21")

    t3 = Television("LG OLED55", 1800.0, 7, 55, "4K")
    t4 = Television("Sony Bravia", 1500.0, 8, 65, "4K")

    discount = 10

    computer = [c1, c2]
    for c in computer:
        c.show_info()
        print(c.get_name())
        print(c.get_price())
        print(c.get_amount())
        print(c.get_ram())
        print(c.get_processor())
        print(c.calculate_counted_price(discount))

    telephone = [t1, t2]
    for t in telephone:
        t.show_info()
        print(t.get_name())
        print(t.get_price())
        print(t.get_amount())
        print(t.get_brand())
        print(t.get_model())
        print(t.calculate_counted_price(discount))

    television = [t3, t4]
    for t in television:
        t.show_info()
        print(t.get_name())
        print(t.get_price())
        print(t.get_amount())
        print(t.get_size())
        print(t.get_resolution())
        print(t.calculate_counted_price(discount))


if __name__ == '__main__':
    main()
