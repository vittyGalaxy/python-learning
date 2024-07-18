class Dress:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

    def get_brand(self):
        return self.brand

    def get_size(self):
        return self.size

    def get_price(self):
        return self.price

    def show_info(self):
        print(f"marca: {self.brand}, taglia: {self.size}, prezzo: {self.price}")

    def dress_type(self):
        pass


class Tshirt(Dress):
    def __init__(self, brand, size, price, material, sleeves):
        super().__init__(brand, size, price)
        self.material = material
        self.sleeves = sleeves

    def get_material(self):
        return self.material

    def get_sleeves(self):
        return self.sleeves

    def show_info(self):
        super().show_info()
        print(f"materiale: {self.material}, maniche: {self.sleeves}")

    def dress_type(self):
        return "Maglietta"


class Trousers(Dress):
    def __init__(self, brand, size, price, length, typee):
        super().__init__(brand, size, price)
        self.length = length
        self.typee = typee

    def get_length(self):
        return self.length

    def get_typee(self):
        return self.typee

    def show_info(self):
        super().show_info()
        print(f"lunghezza: {self.length}, tipo: {self.typee}")

    def dress_type(self):
        return "Pantaloni"


class Jacket(Dress):
    def __init__(self, brand, size, price, color, padding):
        super().__init__(brand, size, price)
        self.color = color
        self.padding = padding

    def get_color(self):
        return self.color

    def get_padding(self):
        return self.padding

    def show_info(self):
        super().show_info()
        print(f"colore: {self.color}, imbottitura: {self.padding}")

    def dress_type(self):
        return "Giacca"


def main():
    t1 = Tshirt("Nike", "M", 29.99, "cotone", "corte")
    t2 = Tshirt("Adidas", "L", 24.99, "poliestere", "lunghe")

    t3 = Trousers("Levi's", "32", 49.99, "lunghi", "jeans")
    t4 = Trousers("Puma", "M", 39.99, "corti", "tuta")

    j1 = Jacket("North Face", "L", 99.99, "nero", "sì")
    j2 = Jacket("Columbia", "M", 89.99, "rosso", "no")

    t_shirt = [t1, t2]
    for t in t_shirt:
        t.show_info()
        print(t.get_brand())
        print(t.get_size())
        print(t.get_price())
        print(t.get_material())
        print(t.get_sleeves())
        print(t.dress_type())

    trousers = [t3, t4]
    for t in trousers:
        t.show_info()
        print(t.get_brand())
        print(t.get_size())
        print(t.get_price())
        print(t.get_length())
        print(t.get_typee())
        print(t.dress_type())

    jacket = [j1, j2]
    for j in jacket:
        j.show_info()
        print(j.get_brand())
        print(j.get_size())
        print(j.get_price())
        print(j.get_color())
        print(j.get_padding())
        print(j.dress_type())


if __name__ == '__main__':
    main()
