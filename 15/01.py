class Car:
    number_of_cars = 0
    info = ''

    def __init__(self, model = 'Toyota', color = 'black'):
        self.model = model
        self.color = color
        self.produce_car()

    @classmethod
    def produce_car(cls):
        cls.number_of_cars += 1

    @classmethod
    def get_info(cls):
        return cls.info

    @classmethod
    def set_info(cls, info):
        cls.info = info


class Truck(Car):
    number_of_cars = 0

    def __init__(self, model='MAN', color='black', weight = 20000):
        super().__init__(model, color)
        self.weight = weight



car1 = Car()
car2 = Car('Mazda')
car3 = Car('KIA', 'white')

print(Car.number_of_cars)
print(car3.number_of_cars)

car4 = Car('Hundai', 'red')
print(Car.number_of_cars)

print('=' * 30)
car5 = Truck()
car6 = Truck(weight=30000)

print(Car.number_of_cars)
print(Truck.number_of_cars)

print('=' * 30)
print(car6.get_info())
car1.set_info(f"I'm a first car. My color is {car1.color}")
print(car6.get_info())