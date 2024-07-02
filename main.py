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
        if random.randint(0, 1) == 0
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