class Car:
    """" Простая модель авто """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """" Возвращает отформатированное описание"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """" Выводит пробег машины в милях """
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """" Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменение отклоняется """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """" Увеличивает показания одометра с заданным приращением """
        self.odometer_reading += miles
