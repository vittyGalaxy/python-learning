if __name__ == '__main__':
    import random
    from disegno import d_impiccato

    liste_parole = ["hello", "world"]
    scelta_parole = random.choice(liste_parole)

    game_over = False
    energia = len(d_impiccato) - 1

    campo_gioco = []
    for i in scelta_parole:
        campo_gioco += '_'

    while not game_over:
        indovina = input('indovina la lettera: ')
        for posizione in range(len(scelta_parole)):
            lettera = scelta_parole[posizione]
            if lettera == indovina:
                campo_gioco[posizione] = lettera
        print(f"{' '.join(campo_gioco)}")

        if indovina not in scelta_parole:
            print(f"Hai tentato con la lettera {indovina}, non e' la lettera corretta. Hai perso una vita.")
            energia -= 1
            if energia == 0:
                game_over = True
                print(f"Hai Perso!. La parola corretta era {scelta_parole}")

        if not '_' in campo_gioco:
            game_over = True
            print('Complimenti hai vinto!')

        print(d_impiccato[energia])