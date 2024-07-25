import numpy as np


def main():
    array = np.array([1, 2, 3])
    number = 4
    result = array + number
    print("Risultato: ", result)

    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([100, 200, 300])
    z = x + y
    print("Z: ", z)

    dataset = np.random.randint(0, 100, size=(5, 3))
    average = dataset.mean(axis=0)
    standard_waste = dataset.std(axis=0)
    normalized_dataset = (dataset - average) / standard_waste
    print("Dataset originale:\n", dataset)
    print("Dataset normalizzato:\n", normalized_dataset)


if __name__ == '__main__':
    main()
