from abc import ABC,abstractmethod


class LibraryElement(ABC):
    def __init__(self, title, publication_year, available=True):
        self.title = title
        self.publication_year = publication_year
        self.available = available

    def get_title(self):
        return self.title

    def get_publication_year(self):
        return self.publication_year

    def get_available(self):
        return self.available

    def show_info(self):
        print(f"titolo: {self.title}, anno di pubblicazione: {self.publication_year}, disponibile: {self.available}")

    def calculate_loan_duration(self):
        pass

    def lend(self):
        if self.available:
            self.available = False

        else:
            print(f"{self.title} non e' disponibile per il prestito")

    def give_back(self):
        self.available = True


class Book(LibraryElement):
    def __init__(self, title, publication_year, author, number_pages, available=True):
        super().__init__(title, publication_year, available)
        self.author = author
        self.number_pages = number_pages

    def get_author(self):
        return self.author

    def get_number_pages(self):
        return self.number_pages

    def show_info(self):
        super().show_info()
        print(f"autore: {self.author}, numero di pagine: {self.number_pages}")

    def calculate_loan_duration(self):
        return 30


class Magazine(LibraryElement):
    def __init__(self, title, publication_year, number, publisher,available=True):
        super().__init__(title, publication_year, available)
        self.number = number
        self.publisher = publisher

    def get_number(self):
        return self.number

    def get_publisher(self):
        return self.publisher

    def show_info(self):
        super().show_info()
        print(f"numero: {self.number}, editore: {self.publisher}")

    def calculate_loan_duration(self):
        return 7


class DVD(LibraryElement):
    def __init__(self, title, publication_year, director, duration, available=True):
        super().__init__(title, publication_year, available)
        self.director = director
        self.duration = duration

    def get_director(self):
        return self.director

    def get_duration(self):
        return self.duration

    def show_info(self):
        super().show_info()
        print(f"regista: {self.director}, durata: {self.duration} minuti")

    def calculate_loan_duration(self):
        return 14


def main():
    b1 = Book("Il Nome della Rosa", 1980, "Umberto Eco", 512)
    b2 = Book("1984", 1949, "George Orwell", 328)

    m1 = Magazine("National Geographic", 2023, 345, "National Geographic Society")
    m2 = Magazine("Time", 2023, 15, "Time USA, LLC")

    d1 = DVD("Inception", 2010, "Christopher Nolan", 148)
    d2 = DVD("Interstellar", 2014, "Christopher Nolan", 169)

    book = [b1, b2]
    for b in book:
        b.show_info()
        print(b.get_title())
        print(b.get_publication_year())
        print(b.get_author())
        print(b.get_number_pages())
        print(b.get_available())
        print(b.calculate_loan_duration())

    magazine = [m1, m2]
    for m in magazine:
        m.show_info()
        print(m.get_title())
        print(m.get_publication_year())
        print(m.get_number())
        print(m.get_publisher())
        print(m.get_available())
        print(m.calculate_loan_duration())

    dvd = [d1, d2]
    for d in dvd:
        d.show_info()
        print(d.get_title())
        print(d.get_publication_year())
        print(d.get_director())
        print(d.get_duration())
        print(d.get_available())
        print(d.calculate_loan_duration())


if __name__ == '__main__':
    main()
