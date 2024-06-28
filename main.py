if __name__ == '__main__':
    import random
    soldi = 100

    def testa_o_croce(puntata, testa_croce):
        lancio = random.randint(0, 1)

        if lancio == 0:
            if testa_croce == "Testa":
                print("Testa, hai vinto! Il tuo saldo e;: " + str(soldi + puntata))

            else:
                print("Testa, hai perso! Il tuo saldo e': " + str(soldi - puntata))

        else:
            if testa_croce == "Croce":
                print("Croce, hai vinto! Il tuo saldo e': " + str(soldi + puntata))

            else:
                print("Croce, hai perso! Il tuo saldo e': " + str(soldi - puntata))

    testa_o_croce(10, "Testa")
    testa_o_croce(10, "Croce")