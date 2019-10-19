from car import Car


class Battery:
    """" Простая модель аккумулятора электромобиля """
    def __init__(self, battery_size=70):
        """" Инициализирует атрибуты аккумулятора """
        self.battery_size = battery_size

    def describe_battery(self):
        """" Выводит информацию о мощности аккумулятора """
        print(f'This car has a {self.battery_size}-kwh battery.')

    def get_range(self):
        """" Выводит приблизительный запас хода для аккумулятора """
        if self.battery_size == 70:
            range = 240
            print(f"This car can go approximately {range} "
                  f"miles on a full charge")
        elif self.battery_size == 85:
            range = 270
            print(f"This car can go approximately {range} "
                  f"miles on a full charge")

    def upgrade_battery(self):
        """" Проверка размера аккумулятора и установление верной мощности """
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """" Представляет аспекты машины, специфические для электромобилей """

    def __init__(self, make, model, year):
        """" Инициализирует атрибуты класса-родителя.
         Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """" У электромобилей нет бензобака """
        print("This car doesn't need a gas tank!")
