class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def print_product(self):
        print("Il nome del prodotto e' " + self.name + " ce ne sono " + str(self.amount) + " e costa " + str(self.price) + " euro")


if __name__ == '__main__':

    p = Product("Cereali", 10, 3)
    p.print_product()