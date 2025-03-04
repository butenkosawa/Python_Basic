# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне,
# або False якщо число непарне, але при цьому НЕ МОЖНА використовувати
# ділення у функції, та дії пов'язані з ним.
# Тобто заборонено використовувати /, //, % та divmod
# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)
# Вхідні дані: Ціле число.
# Вихідні дані: True або False
#
# def is_even(number):
#     pass
#
# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'

def is_even(number):
    return [True, False][int(str(bin(number))[-1])]


number1 = 2494563894038**2
number2 = 1056897**2
number3 = 24945638940387**3

print(is_even(number1))
print(is_even(number2))
print(is_even(number3))
