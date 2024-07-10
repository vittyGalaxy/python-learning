class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def update_author(self, new_author):
        self.author = new_author
        print(f"Autore aggiornato a '{self.author}'")
        return self.author

    def __str__(self):
        return f"Titolo: {self.title}, Autore: {self.author}"


def main():
    t = input("Inserisci il titolo: ")
    a = input("Inserisci l'autore: ")
    b = Book(str(t), str(a))
    print(b.getTitle())
    print(b.getAuthor())
    print(Book(str(t), str(a)))
    a = input("Inserisci un nuovo autore: ")
    print(b.update_author(a))
    print(b.getAuthor())
    print(Book(str(t), str(a)))

if __name__ == '__main__':
    main()