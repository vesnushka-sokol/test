class User:
    def __init__(self, first_name, last_name, familienstand, kinder=0):
        self.f_name = first_name
        self.l_name = last_name
        self.f_stand = familienstand
        self.k = kinder
        self.login_attempts = 0

    def describe_user(self):
        if self.k == 0:
            print(f'{self.f_name.title()} {self.l_name.title()} ist'
                  f' {self.f_stand}, keine Kinder.')
        elif self.k == 1:
            print(f'{self.f_name.title()} {self.l_name.title()} ist'
                  f' {self.f_stand}, hat {self.k} Kind.')
        else:
            print(f'{self.f_name.title()} {self.l_name.title()} ist'
                  f' {self.f_stand}, hat {self.k} Kinder.')

    def greet_uset(self):
        print(f'Guten Tag {self.f_name.title()} {self.l_name.title()}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
