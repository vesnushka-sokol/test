class Angestellter():
    """" Представляет работника """
    def __init__(self, vorname, name, gehalt):
        self.vorname = vorname
        self.name = name
        self.gehalt = gehalt

    def vorstellung(self):
        return f'Меня зовут {self.name} {self.vorname}, я получаю ' \
            f'{self.gehalt} в месяц.'

    def give_raise(self, raise_gehalt=5000):
        self.gehalt += raise_gehalt
        return self.gehalt


men_1 = Angestellter('Alex', 'Sok', 4500)
print(men_1.vorstellung())
print(men_1.give_raise())
print(men_1.vorstellung())
