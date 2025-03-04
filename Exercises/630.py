# Напишіть функцію для підрахунку добутку усіх елементів у списку цілих чисел.
# Вхідні дані:
# 1 10 4 8 11 5 2
# Вихідні дані:
# 35200

def product_of_integers(numbers:list):
    if len(numbers) == 1:
        return numbers.pop()
    return numbers.pop() * product_of_integers(numbers)

print(product_of_integers([1, 10, 4, 8, 11, 5, 2]))