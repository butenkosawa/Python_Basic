class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, new_fullname):
        self.name, self.surname = new_fullname.split()


p1 = Person('Volodymyr', 'Lova')
print(p1.name)
print(p1.surname)
print(p1.fullname)

print('=' * 20)

p1.name = 'Yurii'
print(p1.name)
print(p1.surname)
print(p1.fullname)

print('=' * 20)

p1.fullname = 'Serhii Petrunchak'
print(p1.name)
print(p1.surname)
print(p1.fullname)
