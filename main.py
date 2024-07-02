if __name__ == '__main__':
    import random

    def disegna_tabella(tabella):
        print("   |   |")
        print(" " + tabella[7] + " | " + tabella[8] + " | " + tabella[9])
        print("   |   |")
        print("------------")
        print("   |   |")
        print(" " + tabella[4] + " | " + tabella[5] + " | " + tabella[6])
        print("   |   |")
        print("------------")
        print("   |   |")
        print(" " + tabella[1] + " | " + tabella[2] + " | " + tabella[3])
        print("   |   |")

    disegna_tabella([" "] * 10)

    def letteraGiocatore():
        lettera = ""
        while not(lettera == "X" or lettera == "O"):
            print("Vuoi la X o la O?")
            lettera = input().upper()

        if lettera == "X":
            return ("X", "O")
        else:
            return ("O", "X")

    def chi_inizia():
        if random.randint(0, 1) == 0:
            return "computer"
        else:
            return "giocatore"

    def gioca_ancora():
        print("Vuoi giocare ancora? (s = Si, n = No")
        return input().lower().startswith("s")


    def fai_la_mossa(tabella, lettera, mossa):
        tabella[mossa] = lettera


    def il_vincitore(tabella, lettera):
        return ((tabella[7] == lettera and tabella[8] == lettera and tabella[9] == lettera) or
                (tabella[4] == lettera and tabella[5] == lettera and tabella[6] == lettera) or
                (tabella[1] == lettera and tabella[2] == lettera and tabella[3] == lettera) or
                (tabella[7] == lettera and tabella[4] == lettera and tabella[1] == lettera) or
                (tabella[8] == lettera and tabella[5] == lettera and tabella[2] == lettera) or
                (tabella[9] == lettera and tabella[6] == lettera and tabella[3] == lettera) or
                (tabella[7] == lettera and tabella[5] == lettera and tabella[3] == lettera) or
                (tabella[9] == lettera and tabella[5] == lettera and tabella[1] == lettera))

    def spazio_libero(tabella, mossa):
        return tabella[mossa] == " "

    def crea_copia_tabella(tabella):
        copiaTab = []
        for i in tabella:
            copiaTab.append(i)
        return copiaTab

    def mossa_giocatore(tabella):
        mossa = " "
        while mossa not in "1 2 3 4 5 6 7 8 9".split() or not spazio_libero(tabella, int(mossa)):
            print("Quale sara' la tua prossima mossa? (1-9)")
            mossa = input()
        return int(mossa)

    def fai_mossa_casuale_da_list(tabella, lista_mosse):
        possibili_mosse = []
        for i in lista_mosse:
            if spazio_libero(tabella, i):
                possibili_mosse.append(i)

        if len(possibili_mosse) != 0:
            return random.choice(possibili_mosse)
        else:
            return None

    def mossa_computer(tabella, lettera_computer):
        if lettera_computer == "X":
            lettera_giocatore = "O"
        else:
            lettera_giocatore = "X"

        for i in range(1, 10):
            copia = crea_copia_tabella(tabella)
            if spazio_libero(copia, i):
                fai_la_mossa(copia, lettera_computer, i)
                if il_vincitore(copia, lettera_computer):
                    return i

        for i in range(1, 10):
            copia = crea_copia_tabella(tabella)
            if spazio_libero(copia, i):
                fai_la_mossa(copia, lettera_giocatore, i)
                if il_vincitore(copia, lettera_giocatore):
                    return i

        mossa = fai_mossa_casuale_da_list(tabella, [1, 3, 7, 9])
        if mossa != None:
            return mossa

        if spazio_libero(tabella, 5):
            return 5

        return fai_mossa_casuale_da_list(tabella, [2, 4, 6, 8])

    def tabella_completa(tabella):
        for i in range(1, 10):
            if spazio_libero(tabella, i):
                return False
            else:
                return True

    print("Benvenuto a Tris!")

    while True:
        la_tabella = [" "] * 10
        lettera_giocatore, lettera_computer = letteraGiocatore()
        turno = chi_inizia()
        print("Il " + turno + " parte per primo.")
        partita_corso = True

        while partita_corso:
            if turno == "giocatore":
                disegna_tabella(la_tabella)
                mossa = mossa_giocatore(la_tabella)
                fai_la_mossa(la_tabella, lettera_giocatore, mossa)

                if il_vincitore(la_tabella, lettera_giocatore):
                    disegna_tabella(la_tabella)
                    print("Evviva! Hai vinto")
                    partita_corso = False
                else:
                    if tabella_completa(la_tabella):
                        disegna_tabella(la_tabella)
                        print("La partita e' finita in parita'.")
                        break
                    else:
                        turno = "computer"
            else:
                mossa = mossa_computer(la_tabella, lettera_computer)
                fai_la_mossa(la_tabella, lettera_computer, mossa)

                if il_vincitore(la_tabella, lettera_computer):
                    disegna_tabella(la_tabella)
                    print("Il computer ti ha sconfitto. Hai perso!")
                    partita_corso = False
                else:
                    if tabella_completa(la_tabella):
                        disegna_tabella(la_tabella)
                        print("La partita e' finita in parita'.")
                        break
                    else:
                        turno = "giocatore"

        if not gioca_ancora():
            break