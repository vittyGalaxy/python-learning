class BankAccount:
    def __init__(self, holder, balance = 0):
        self.holder = holder
        self.balance = balance
    def getHolder(self):
        return self.holder

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Hai depositato {amount} euro, Il saldo attuale e': {self.balance} euro")

        else:
            print("L'importo del deposito deve essere positivo.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Hai prelevato {amount} euro, Il saldo attuale e':{self.balance} euro")

            else:
                print("Saldo insufficiente per il prelievo")

        else:
            print("L'importo del prelievo deve essere positivo.")


def main():
    b = BankAccount("Vittorio Tiozzo")
    print(b.getHolder())
    print(b.getBalance())
    print(BankAccount("Vittorio Tiozzo"))
    b.deposit(100)
    b.withdraw(50)
    print(b.getBalance())

    b.withdraw(100)
    b.withdraw(-3)
    b.deposit(-5)


if __name__ == '__main__':
    main()