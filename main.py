class Material:
    def __init__(self, title, authors, year_publication):
        self.title = title
        self.authors = authors
        self.year_publication = year_publication

    def get_title(self):
        return self.title

    def get_authors(self):
        return self.authors

    def get_year_publication(self):
        return self.year_publication

    def show_info(self):
        print(f"titolo: {self.title}, autori: {self.authors}, anno di pubblicazione: {self.year_publication}")


class Book(Material):
    def __init__(self, title, authors, year_publication, number_of_pages, genre):
        super().__init__(title, authors, year_publication)
        self.number_of_pages = number_of_pages
        self.genre = genre

    def get_number_of_pages(self):
        return self.number_of_pages

    def get_genre(self):
        return self.genre

    def show_info(self):
        super().show_info()
        print(f"numero di pagine: {self.number_of_pages}, genere: {self.genre}")


class Magazine(Material):
    def __init__(self, title, authors, year_publication, number, publication_month):
        super().__init__(title, authors, year_publication)
        self.number = number
        self.publication_month = publication_month

    def get_publication_month(self):
        return self.publication_month

    def get_number(self):
        return self.number

    def show_info(self):
        super().show_info()
        print(f"numero: {self.number}, mese di pubblicazione: {self.publication_month}")


class DVD(Material):
    def __init__(self, title, authors, year_publication, duration, genre):
        super().__init__(title, authors, year_publication)
        self.duration = duration
        self.genre = genre

    def get_duration(self):
        return self.duration

    def get_genre(self):
        return self.genre

    def show_info(self):
        super().show_info()
        print(f"durata: {self.duration}, genere: {self.genre}")


def main():
    b1 = Book("Il Signore degli Anelli", ["J.R.R. Tolkien"], 1954, 1216, "Fantasy")
    b2 = Book("1984", ["George Orwell"], 1949, 328, "Distopia")

    m1 = Magazine("National Geographic", ["Vari autori"], 2023, 501, "Luglio")
    m2 = Magazine("Scientific American", ["Vari autori"], 2023, 1023, "Agosto")

    d1 = DVD("Inception", ["Christopher Nolan"], 2010, 148, "Fantascienza")
    d2 = DVD("Il Padrino", ["Francis Ford Coppola"], 1972, 175, "Dramma")

    book = [b1, b2]
    for b in book:
        b.show_info()
        print(b.get_title())
        print(b.get_authors())
        print(b.get_year_publication())
        print(b.get_number_of_pages())
        print(b.get_genre())

    magazine = [m1, m2]
    for m in magazine:
        m.show_info()
        print(m.get_title())
        print(m.get_authors())
        print(m.get_year_publication())
        print(m.get_number())
        print(m.get_publication_month())

    dvd = [d1, d2]
    for d in dvd:
        d.show_info()
        print(d.get_title())
        print(d.get_authors())
        print(d.get_year_publication())
        print(d.get_duration())
        print(d.get_genre())


if __name__ == '__main__':
    main()
