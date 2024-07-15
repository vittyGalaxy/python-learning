class Media:
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

    def get_title(self):
        return self.title

    def get_publication_year(self):
        return self.publication_year

    def show_info(self):
        print(f"Titolo: {self.publication_year}, anno di pubblicazione: {self.publication_year}")


class Book(Media):
    def __init__(self, title, publication_year, author, number_pages):
        super().__init__(title, publication_year)
        self.author = author
        self.number_pages = number_pages

    def get_author(self):
        return self.author

    def get_number_pages(self):
        return self.number_pages

    def show_info(self):
        super().show_info()
        print(f"Autore: {self.author}, Numero pagine: {self.number_pages}")


class Film(Media):
    def __init__(self, title, publication_year, director, duration):
        super().__init__(title, publication_year)
        self.director = director
        self.duration = duration

    def get_director(self):
        return self.director

    def get_duration(self):
        return self.duration

    def show_info(self):
        super().show_info()
        print(f"Regista: {self.director}, Durata: {self.duration}")


class LibraryManagement:
    def __init__(self):
        self.media_list = []

    def add_media(self, media):
        if isinstance(media, Media):
            self.media_list.append(media)

    def remove_media(self, title):
        self.media_list = [media for media in self.media_list if media.title != title]

    def print_descriptions(self):
        for media in self.media_list:
            print(media.show_info())

    def search_media(self, title):
        for media in self.media_list:
            if media.title == title:
                return media

        return None


def main():
    b1 = Book("1984", 1949, "George Orwell", 328)
    b2 = Book("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1216)
    f1 = Film("Inception", 2010, "Christopher Nolan", 148)
    f2 = Film("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", 136)
    b1.show_info()
    print()
    b2.show_info()
    print()
    f1.show_info()
    print()
    f2.show_info()

    print(b1.get_title())
    print(b1.get_publication_year())
    print(b1.get_author())
    print(b1.get_number_pages())
    print(b2.get_title())
    print(b2.get_publication_year())
    print(b2.get_author())
    print(b2.get_number_pages())
    print(f1.get_title())
    print(f1.get_publication_year())
    print(f1.get_director())
    print(f1.get_duration())
    print(f2.get_title())
    print(f2.get_publication_year())
    print(f2.get_director())
    print(f2.get_duration())
    print()

    library = LibraryManagement()
    library.add_media(b1)
    library.add_media(b2)
    library.add_media(f1)
    library.add_media(f2)

    print("Descrizioni dei media nella bibblioteca: ")
    library.print_descriptions()

    media = library.search_media("Inception")
    if media:
        print(media.show_info())

    else:
        print("Media non trovato.")

    library.remove_media("1984")
    print("\nDescrizioni dopo aver rimosso '1984': ")
    library.print_descriptions()


if __name__ == '__main__':
    main()
