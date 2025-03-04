# Існує функція coffee(), яка варить каву і якщо її викликати, то вона друкує
# "кава".
# Написати декоратор та декорувати цю функцію так, щоб можна було варити каву
# з цукром, молоком або тим та іншим водночас. Також можна заварити подвійну
# каву, або каву з подвійним молоком, чи подвійним цукром. Якщо виклакити
# задекоровану функцію без аргументів, то вона зварить звичайну каву, так
# наче функція не декорована. При чому ніяких змін до самої функції coffee()
# вносити не можна.
#
# Приклад виклику не декорованої функції:
# def coffe():
#     print('кава')
#
# print(coffe())  # Результат: 'кава'
#
#
# Приклад виклику декорованої функції:
# @decorator
# def coffe():
#     print('кава')
#
# coffe()  # Результат: 'кава'
# coffe(double=True)  # Результат: 'подвійна кава'
# coffe(milk=1)  # Результат: 'з молоком кава'
# coffe(milk=1, suger=1)  # Результат: 'з молоком та цукром кава'
# coffe(suger=1)  # Результат: 'з цукром кава'
# coffe(milk=2, suger=1, double=True)  # Результат: 'з подвійним молоком та цукром подвійна кава'
# coffe(suger=2, double=True)  # Результат: 'з подвійним цукром подвійна кава'
# coffe(milk=2, suger=2, double=False)  # Результат: 'з подвійним молоком та подвійним цукром кава'
#
# * Зверніть увагу на те, що результат завжди виводиться у одну строку.

def coffe_machine(function):
    def wrapper(milk = 0, sugar = 0, double = False):
        coffe_milk = ''
        coffe_sugar = ''
        coffe_double = ''

        if double is True:
            coffe_double = 'подвійна'

        if sugar == 1:
            coffe_sugar = 'з цукром'
        elif sugar == 2:
            coffe_sugar = 'з подвійним цукром'

        if milk == 1:
            coffe_milk = 'з молоком'
            if sugar == 1:
                coffe_sugar = 'та цукром'
            elif sugar == 2:
                coffe_sugar = 'та подвійним цукром'
        elif milk == 2:
            coffe_milk = 'з подвійним молоком'
            if sugar == 1:
                coffe_sugar= 'та цукром'
            elif sugar == 2:
                coffe_sugar = 'та подвійним цукром'

        result = (coffe_milk + ' ' + coffe_sugar + ' ' + coffe_double).strip()

        if result != '':
            print(result, end=' ')

        function(milk = 0, sugar = 0, double = False)

    return wrapper

@coffe_machine
def coffe(milk = 0, sugar = 0, double = False):
    print('кава')


coffe()  # Результат: 'кава'
coffe(double=True)  # Результат: 'подвійна кава'
coffe(milk=1)  # Результат: 'з молоком кава'
coffe(milk=1, sugar=1)  # Результат: 'з молоком та цукром кава'
coffe(sugar=1)  # Результат: 'з цукром кава'
coffe(milk=2, sugar=1, double=True)  # Результат: 'з подвійним молоком та цукром подвійна кава'
coffe(sugar=2, double=True)  # Результат: 'з подвійним цукром подвійна кава'
coffe(milk=2, sugar=2, double=False)  # Результат: 'з подвійним молоком та подвійним цукром кава'