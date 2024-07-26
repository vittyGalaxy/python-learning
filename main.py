import numpy as np


def main():
    date = np.array([10, 20, 30, 40, 50])
    print("Media: ", np.mean(date))
    print("Mediana: ", np.median(date))
    print("Deviazione standard: ", np.std(date))
    print("Varianaza: ", np.var(date))

    print("Deviazione standard (campione): ", np.std(date, ddof=1))
    print("Varianza (campione): ", np.var(date, ddof=1))

    print("Minimo: ", np.min(date), "Massimo: ", np.max(date))
    print("Somma totale: ", np.sum(date), "Prodotto totale: ", np.prod(date))


if __name__ == '__main__':
    main()
