if __name__ == '__main__':
    import random

    liste_parole = ["hello", "world"]
    scelta_parole = random.choice(liste_parole)

    game_over = False

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

        if not '_' in campo_gioco:
            game_over = True
            print('Complimenti hai vinto!')

    print(scelta_parole)
