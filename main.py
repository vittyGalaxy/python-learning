if __name__ == '__main__':
    def eta(num):
        if num < 18:
            print("Sei minorenne")
        else:
            print("Sei maggiorenne")

    eta(15)
    eta(19)

    def anni(num):
        if num < 10:
            print("Sei un bambino")
        elif num < 18:
            print("Sei quasi maggiorenne")
        else:
            print("Sei maggiorenne")

    anni(16)
    anni(9)
    anni(20)
