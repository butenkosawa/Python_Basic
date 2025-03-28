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

            # Рішення викладача:


class Negative_degree(Exception):
    def __init__(self, message='Зведення у негативний ступінь'):
        super().__init__(message)


class Calculator(int):

    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        try:
            return Calculator(self.var + other)
        except TypeError:
            return 'Не можна складати цифри та літери!'

    def __sub__(self, other):
        try:
            return Calculator(self.var - other)
        except TypeError:
            return 'Не можна від цифри відібрати літери!'

    def __pow__(self, power, modulo=None):
        try:
                if power >= 0:
                    return Calculator(self.var ** power)
                else:
                    raise Negative_degree()
        except Negative_degree:
            return 'Зведення у негативний ступінь заборонено!'

    def __truediv__(self, other):
        try:
            return Calculator(self.var / other)
        except ZeroDivisionError:
            return 'Не можна ділити на нуль!'
        except TypeError:
            return 'Не можна ділити на літери!'
