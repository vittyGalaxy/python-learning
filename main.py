class Book:
    def __init__(self, title, author, price, quantity):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def show_info(self):
        print(f"nome: {self.title}, autore: {self.author}, prezzo: {self.price}, quantita': {self.quantity}")

    def calculate_total_price(self, n_copies):
        if n_copies > self.quantity:
            return "Quantita' non disponibile"

        return round(self.price * n_copies, 2)


class Storytelling(Book):
    def __init__(self, title, author, price, quantity, genre):
        super().__init__(title, author, price, quantity)
        self.genre = genre

    def get_genre(self):
        return self.genre

    def show_info(self):
        super().show_info()
        print(f"genere: {self.genre}")


class Nonfiction(Book):
    def __init__(self, title, author, price, quantity, topic):
        super().__init__(title, author, price, quantity)
        self.topic = topic

    def get_topic(self):
        return self.topic

    def show_info(self):
        super().show_info()
        print(f"argomento: {self.topic}")


class TechnicalManual(Book):
    def __init__(self, title, author, price, quantity, field, level):
        super().__init__(title, author, price, quantity)
        self.field = field
        self.level = level

    def get_field(self):
        return self.field

    def get_level(self):
        return self.level

    def show_info(self):
        super().show_info()
        print(f"campo: {self.field}, livello: {self.level}")


def main():
    s1 = Storytelling("Il Grande Gatsby", "F. Scott Fitzgerald", 15.0, 20, "Romanzo")
    s2 = Storytelling("1984", "George Orwell", 12.0, 15, "Distopia")

    n1 = Nonfiction("Sapiens", "Yuval Noah Harari", 20.0, 10, "Storia")
    n2 = Nonfiction("Il Gene", "Siddhartha Mukherjee", 18.0, 8, "Biologia")

    t1 = TechnicalManual("Python per tutti", "Mark Lutz", 25.0, 5, "Programmazione", "Intermedio")
    t2 = TechnicalManual("Introduzione alla Data Science", "Joel Grus", 30.0, 3, "Data Science", "Base")

    n_copies = 3

    storytelling = [s1, s2]
    for s in storytelling:
        s.show_info()
        print(s.get_title())
        print(s.get_author())
        print(s.get_price())
        print(s.get_quantity())
        print(s.get_genre())
        print(s.calculate_total_price(n_copies))

    nonfiction = [n1, n2]
    for n in nonfiction:
        n.show_info()
        print(n.get_title())
        print(n.get_author())
        print(n.get_price())
        print(n.get_quantity())
        print(n.get_topic())
        print(n.calculate_total_price(n_copies))

    technical_manual = [t1, t2]
    for t in technical_manual:
        t.show_info()
        print(t.get_title())
        print(t.get_author())
        print(t.get_price())
        print(t.get_quantity())
        print(t.get_field())
        print(t.get_level())
        print(t.calculate_total_price(n_copies))


if __name__ == '__main__':
    main()
