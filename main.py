if __name__ == '__main__':
    abilita = ["comunicazione", "memoria", "ragionamento", "concentrazione"]
    voti = [87, 95, 89, 75]
    abilita.append("agilita mentale")
    voti.append(80)
    unione = list(zip(abilita, voti))
    print(unione)