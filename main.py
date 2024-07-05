import csv

if __name__ == '__main__':
    elenco_nomi = [{"Nome": "Vittorio", "Cognome": "Tiozzo", "Email": "vittorio@gmail.com"}]
    int_colonne = ["Nome", "Cognome", "Email"]

    # with open("file.csv", "w") as nomi_elenco:
    #     scrittura = csv.DictWriter(nomi_elenco, fieldnames = int_colonne)
    #
    #     scrittura.writeheader()
    #
    #     for elemento in elenco_nomi:
    #         scrittura.writerow(elemento)

    with open("file.csv") as elenco:
        content = elenco.read()

        print(content)