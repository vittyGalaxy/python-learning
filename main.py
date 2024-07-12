class Account:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def show_info(self):
        print(f"Username: {self.username}, Email: {self.email}")


class AccountStandard(Account):
    def show_info(self):
        super().show_info()
        print("Tipo di account: Standard")


class AdministratorAccount(Account):
    def __init__(self, username, email, privileges):
        super().__init__(username, email)
        self.privileges = privileges

    def show_info(self):
        super().show_info()
        print(f"Tipo di account: Amministratore, privilegi: {', '.join(self.privileges)}")


def main():
    a_s = AccountStandard("utente_standard", "standard@example.com")
    a_a = AdministratorAccount("admin", "admin@example.com", ["gestione utenti", "accesso completo"])
    a_s.show_info()
    print()
    a_a.show_info()


if __name__ == '__main__':
    main()
