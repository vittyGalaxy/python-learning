class Product:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def show_info(self):
        print(f"titolo: {self.title}, autore: {self.author}, prezzo: {self.price}")


class Book(Product):
    def __init__(self, title, author, price, number_pages, cover):
        super().__init__(title, author, price)
        self.number_pages = number_pages
        self.cover = cover

    def get_number_pages(self):
        return self.number_pages

    def get_cover(self):
        return self.cover

    def show_info(self):
        super().show_info()
        print(f"numero pagine: {self.number_pages}, copertina: {self.cover}")


class EBook(Product):
    def __init__(self, title, author, price, file_size, formatt):
        super().__init__(title, author, price)
        self.file_size = file_size
        self.formatt = formatt

    def get_file_size(self):
        return self.file_size

    def get_formatt(self):
        return self.formatt

    def show_info(self):
        super().show_info()
        print(f"dimensione file: {self.file_size}, formato: {self.formatt}")


def main():
    l1 = Book("Il Signore degli Anelli", "J.R.R. Tolkien", 20.99, 1178, "rigida")
    l2 = Book("1984", "George Orwell", 12.99, 328, "flessibile")
    e1 = EBook("Il Codice Da Vinci", "Dan Brown", 9.99, 1.5, "PDF")
    e2 = EBook("Harry Potter e la Pietra Filosofale", "J.K. Rowling", 7.99, 2.0, "ePub")

    l1.show_info()
    print()
    l2.show_info()
    print()
    e1.show_info()
    print()
    e2.show_info()
    print()

    print(l1.get_title())
    print(l1.get_author())
    print(l1.get_price())
    print(l1.get_number_pages())
    print(l1.get_cover())

    print(l2.get_title())
    print(l2.get_author())
    print(l2.get_price())
    print(l2.get_number_pages())
    print(l2.get_cover())

    print(e1.get_title())
    print(e1.get_author())
    print(e1.get_price())
    print(e1.get_file_size())
    print(e1.get_formatt())

    print(e2.get_title())
    print(e2.get_author())
    print(e2.get_price())
    print(e2.get_file_size())
    print(e2.get_formatt())


if __name__ == '__main__':
    main()
