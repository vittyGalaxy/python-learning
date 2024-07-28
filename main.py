import numpy as np


def main():
    temperature = np.random.uniform(low=0, high=40, size=365)

    average_temperature = np.mean(temperature)
    max_temperature = np.max(temperature)
    min_temperature = np.min(temperature)
    print(f"Temperatura media: {average_temperature:.2f} gradi")
    print(f"Temperatura massima: {max_temperature:.2f} gradi")
    print(f"Temperatura minima: {min_temperature:.2f} gradi")

    hot_days = np.where(temperature > 30)[0]
    number_of_hot_days = len(hot_days)
    print(f"Giorni con temperatura > 30 gradi: {number_of_hot_days}")


if __name__ == '__main__':
    main()
