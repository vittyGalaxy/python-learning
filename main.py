if __name__ == '__main__':

    libri = "Tentazioni: Aldo Bruno: 1990, Attacco cartico: Marino Carra: 1988, Santo subito!: Gio Batta:2001, Sempre tuo: Stefano Cosmi: 1997"
    lista_libri = libri.split(",")
    print(lista_libri)

    lista_libri_dettagli = []

    for libro in lista_libri:
        lista_libri_dettagli.append(libro.split(":"))

    print(lista_libri_dettagli)

    titolo = []
    autore = []
    data = []

    for libro in lista_libri_dettagli:
        titolo.append(libro[0])
        autore.append(libro[1])
        data.append(libro[2])

    print(titolo, autore, data)

    for i in range(0, len(lista_libri_dettagli)):
        print("Il libro\"{}\" e' stato scrittto da {} nel {} .\n".format(titolo[i], autore[i], data[i]))
