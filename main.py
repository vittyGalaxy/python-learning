if __name__ == '__main__':
    import random

    soldi = 100


    def testa_o_croce(puntata, testa_croce):
        global soldi
        lancio = random.randint(0, 1)
        if lancio == 0:
            if testa_croce == "Testa":
                soldi += puntata
                print("Testa, hai vinto! Il tuo saldo e: " + str(soldi) + ".")

            else:
                soldi -= puntata
                print("Testa, hai perso! Il tuo saldo e': " + str(soldi) + ".")

        else:
            if testa_croce == "Croce":
                soldi += puntata
                print("Croce, hai vinto! Il tuo saldo e': " + str(soldi) + ".")

            else:
                soldi -= puntata
                print("Croce, hai perso! Il tuo saldo e': " + str(soldi) + ".")


    num = input("Scrivi 0 per smettere di giocare oppure un qualsiasi numero per continuare: ")
    while (num != 0) and (soldi >= 0):
        punta = input("Inserisci quanto punti: ")
        t_c = input("Inserisci 'Testa' o 'Croce': ")

        testa_o_croce(int(punta), str(t_c))

        num = input("Scrivi 0 per smettere di giocare oppure un qualsiasi numero per continuare: ")
        if soldi <= 0:
            print("Hai finito i soldi")

    print("Grazie per aver giocato!")