from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        i = 1
        while i != 11:
            x = randint(1, self.sides)
            print(f'{i}-й бросок кубика -- {x}')
            i += 1


kubik = Die
# kubik.roll_die(Die())

kubuk2 = Die(10)
# kubuk2.roll_die()
kubik3 = Die(20)
kubik3.roll_die()
