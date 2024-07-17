class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def show_info(self):
        print(f"nome: {self.name}, prezzo: {self.price}, quantita: {self.quantity}")


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty, brand):
        super().__init__(name, price, quantity)
        self.warranty = warranty
        self.brand = brand

    def get_warranty(self):
        return self.warranty

    def get_brand(self):
        return self.brand

    def show_info(self):
        super().show_info()
        print(f"garanzia: {self.warranty}, marca: {self.brand}")


class Clothing(Product):
    def __init__(self, name, price, quantity, size, material):
        super().__init__(name, price, quantity)
        self.size = size
        self.material = material

    def get_size(self):
        return self.size

    def get_material(self):
        return self.material

    def show_info(self):
        super().show_info()
        print(f"taglia: {self.size}, materiale: {self.material}")


def main():
    e1 = Electronics("Smartphone", 599.99, 10, 2, "Samsung")
    e2 = Electronics("Laptop", 899.99, 5, 3, "Dell")
    c1 = Clothing("T-shirt", 19.99, 50, "M", "Cotone")
    c2 = Clothing("Jeans", 49.99, 30, "L", "Denim")

    e1.show_info()
    print()
    e2.show_info()
    print()
    c1.show_info()
    print()
    c2.show_info()
    print()

    print(e1.get_name())
    print(e1.get_price())
    print(e1.get_quantity())
    print(e1.get_warranty())
    print(e1.get_brand())

    print(e2.get_name())
    print(e2.get_price())
    print(e2.get_quantity())
    print(e2.get_warranty())
    print(e2.get_brand())

    print(c1.get_name())
    print(c1.get_price())
    print(c1.get_quantity())
    print(c1.get_size())
    print(c1.get_material())

    print(c2.get_name())
    print(c2.get_price())
    print(c2.get_quantity())
    print(c2.get_size())
    print(c2.get_material())


if __name__ == '__main__':
    main()
