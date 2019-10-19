class Dog:
    """" Простая модель собаки """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """" Собака садится по команде """
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        """" Собака перекатывается по команде """
        print(f'{self.name.title()} rolled over!')


my_dog = Dog('Boy', 8)
your_dog = Dog('Lusi', 2)
print(f"My dog's name is {my_dog.name.title()}.")
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()
print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f'Your dog is {your_dog.age} years old.')
your_dog.sit()
