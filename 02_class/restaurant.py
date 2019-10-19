class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.kuche = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.name.title()} hat {self.kuche}e Küche.')

    def open_restaurant(self):
        print(f'{self.name.title()} ist geöffnet.')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num
