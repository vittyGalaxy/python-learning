if __name__ == '__main__':
    import random

    liste_parole = ["hello", "world"]
    scelta_parole = random.choice(liste_parole)

    indovina = input('indovina la lettera: ')

    for l in scelta_parole:
        if l == indovina:
            print('Lettera azzeccata')
        else:
            print('Lettera non azzeccata')

    campo_gioco = []
    for i in scelta_parole:
        campo_gioco += '_'

    for posizione in range(len(scelta_parole)):
        lettera = scelta_parole[posizione]
        if lettera == indovina:
            campo_gioco[posizione] = lettera

    print(campo_gioco)

    print(scelta_parole)
