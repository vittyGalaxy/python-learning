if __name__ == '__main__':

    a = [155, 160, 153, 146, 149]
    altezze = [alt for alt in a if alt > 150]
    print(altezze)

    a = [5, 2, 8, 12, 3]
    b = [x * 2 for x in a]
    print(b)