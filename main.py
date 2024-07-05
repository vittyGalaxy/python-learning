class User:
    admin = False
    def __init__(self, name_user):
        self.name_user = name_user


class Admin(User):
    admin = True


if __name__ == '__main__':
    print(issubclass(Admin, User))