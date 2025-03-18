# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум
# додавання, віднімання, ділення, множення, зведення в ступінь та вилучення
# квадратного кореня. Обернути кожен метод у блок try/except і зробити обробку
# кількох винятків, як мінімум ділення на 0. Створити свій виняток, наприклад,
# зведення в негативний ступінь.

class Calculate:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        try:
            return self.number/other.number
        except ZeroDivisionError as err:
            print(err)

    def __pow__(self, power, modulo=None):
        pass

    def expon(self, other):
        try:
            assert other.number > 0, 'Raising to a negative power is not possible'
            return self.number ** other.number
        except AssertionError as err:
            print(err)
