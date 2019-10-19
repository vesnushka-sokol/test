from user import User


class Privileges:
    def __init__(self):
        self.privileges = ['разрешено добавлять сообщения',
                           'разрешено удалять пользователей',
                           'разрешено банить пользователей']

    def show_privileges(self):
        """" Вывод набора привилегий администратора """
        print('Права администратора:')
        for i in self.privileges:
            print(i)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name, familienstand='verheiratet')
        self.privileges = Privileges()
