import numpy as np


def main():
    date = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    mask = date > 5
    print("Machera: ", mask)

    filtered_date = date[mask]
    print("Dati filtrati: ", filtered_date)

    modifield_date = np.where(date < 5, 0, date)
    print("Dati modificati: ", modifield_date)


if __name__ == '__main__':
    main()
