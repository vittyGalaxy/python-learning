class message:
    admin = False
    def __init__(self, sender, object, text):
        self.sender = sender
        self.object = object
        self.text = text


class User:
    def __init__(self, name_user):
        self.name_user = name_user

    def edit_message(self, message, new_text):
        if message.sender == self.name_user:
            message.text = new_text

class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text




if __name__ == '__main__':
