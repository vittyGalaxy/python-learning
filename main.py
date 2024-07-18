class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def show_info(self):
        print(f"nome: {self.name}, prezzo: {self.price}")


class FreshProduct(Product):
    def __init__(self, name, price, expiration_date, origin):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.origin = origin

    def get_expiration_date(self):
        return self.expiration_date

    def get_origin(self):
        return self.origin

    def show_info(self):
        super().show_info()
        print(f"data di scadenza: {self.expiration_date}, origine: {self.origin}")


class PackagedProduct(Product):
    def __init__(self, name, price, weight, ingredients):
        super().__init__(name, price)
        self.weight = weight
        self.ingredients = ingredients

    def get_weight(self):
        return self.weight

    def get_ingredients(self):
        return self.ingredients

    def show_info(self):
        super().show_info()
        print(f"peso: {self.weight}, ingredienti: {self.ingredients}")


def main():
    f1 = FreshProduct("Mela", 1.5, "10/07/2024", "Italia")
    f2 = FreshProduct("Pasta", 0.99, 500, ["Semola di grano duro"])

    p1 = PackagedProduct("Pesce", 10.99, "15/07/2024", "Mare del Nord")
    p2 = PackagedProduct("Biscotti", 2.49, 300, ["Farina", "Zucchero", "Burro"])

    freshProduct = [f1, f2]
    for f in freshProduct:
        f.show_info()
        print(f.get_name())
        print(f.get_price())
        print(f.get_expiration_date())
        print(f.get_origin())

    packaged_product = [p1, p2]
    for p in packaged_product:
        p.show_info()
        print(p.get_name())
        print(p.get_price())
        print(p.get_weight())
        print(p.get_ingredients())


if __name__ == '__main__':
    main()
