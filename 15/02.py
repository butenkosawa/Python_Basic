class Car:

    def __init__(self, model = 'Toyota', color = 'black'):
        self.model = model
        self.color = color

    def __getattr__(self, item):
        print(f'Atribute {item} is absent')
        return None

car2 = Car('Mazda')

print(car2.model)
print(car2.year)