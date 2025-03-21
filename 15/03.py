class Car:

    def __init__(self, model = 'Toyota', color = 'black'):
        self.model = model
        self.color = color

    # def __getattr__(self, item):
    #     print(f'Atribute {item} is absent')
    #     return None

car2 = Car('Mazda')
print(getattr(car2, 'model', ''))
print(getattr(car2, 'color', ''))
print(getattr(car2, 'year', 'none'))
print('=' * 20)
print(hasattr(car2, 'model'))
print(hasattr(car2, 'year'))
