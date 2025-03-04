# Напишіть функцію, яка може генерувати та друкувати кортеж зі значеннями квадратів чисел від 1 до n включно.
# Вхідні дані:
# 6
# Вихідні дані:
# (1, 4, 9, 16, 25, 36)

def create_square_tuple(n: int):
    return tuple([i ** 2 for i in range(1, n+1)])


print(create_square_tuple(6))