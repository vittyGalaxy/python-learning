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


class Telephone(Product):
    def __init__(self, brand, model, price, memory):
        super().__init__(brand, model, price)
        self.memory = memory

    def get_memory(self):
        return self.memory

    def show_info(self):
        super().show_info()
        print(f"memoria: {self.memory}")

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 100)


class Laptop(Product):
    def __init__(self, brand, model, price, ram, storage):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def get_ram(self):
        return self.ram

    def get_storage(self):
        return self.storage

    def show_info(self):
        super().show_info()
        print(f"ram: {self.ram}, storage: {self.storage}")

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 100)


class Tablet(Product):
    def __init__(self, brand, model, price, screen_size):
        super().__init__(brand, model, price)
        self.screen_size = screen_size

    def get_screen_size(self):
        return self.screen_size

    def show_info(self):
        super().show_info()
        print(f"dimensioni schermo: {self.screen_size}")

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 100)


def main():
    t1 = Telephone("Apple", "iPhone 12", 999.99, 128)
    t2 = Telephone("Samsung", "Galaxy S21", 899.99, 256)

    l1 = Laptop("Dell", "XPS 15", 1999.99, 16, 512)
    l2 = Laptop("HP", "Spectre x360", 1599.99, 8, 256)

    t3 = Tablet("Apple", "iPad Pro", 799.99, 12.9)
    t4 = Tablet("Samsung", "Galaxy Tab S7", 649.99, 11.0)

    discount = 10

    telephone = [t1, t2]
    for t in telephone:
        t.show_info()
        print(t.get_brand())
        print(t.get_model())
        print(t.get_price())
        print(t.get_memory())
        print(t.calculate_discount(discount))

    laptop = [l1, l2]
    for l in laptop:
        l.show_info()
        print(l.get_brand())
        print(l.get_model())
        print(l.get_price())
        print(l.get_ram())
        print(l.get_storage())
        print(l.calculate_discount(discount))

    tablet = [t3, t4]
    for t in tablet:
        t.show_info()
        print(t.get_brand())
        print(t.get_model())
        print(t.get_price())
        print(t.get_screen_size())
        print(t.calculate_discount(discount))


if __name__ == '__main__':
    main()
