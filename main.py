def converter(d, h, m):
    s = (m * 60) + (h * 3600) + (d * 86400)
    return s

if __name__ == '__main__':

    days = input("Inserisci i giorni: ")
    hours = input("Inserisci le ore: ")
    minutes = input("Inserisci i minuti: ")
    print("I secondi sono: ", converter(days, hours, minutes))