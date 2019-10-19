from car import Car
from electric_car import ElectricCar

my_new_car = Car('nissan', 'qaskai', 2018)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 29
my_new_car.read_odometer()
print()
my_tesla = ElectricCar('tesla', 'new 1', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
