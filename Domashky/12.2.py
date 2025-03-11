# Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу. Створіть
# клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові,
# мобільний телефон і т.д. Створіть клас "Замовлення". Замовлення може містити
# кілька товарів, причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення. Визначте метод
# str() для коректного виведення інформації про це замовлення.

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        choice = ''
        for item, cnt in self.products.items():
            choice += f"{item.name}: {cnt} pcs.\n"
        return f"User: {self.user}\nItems:\n{choice}".strip()

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt
        return total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5
print("-" * 30)
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov
print("-" * 30)
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())
print("-" * 30)
print(isinstance(cart.user, User))
print("-" * 30)
cart.add_item(apple, 10)
print(cart)
print(cart.get_total())
