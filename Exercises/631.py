# Напишіть функцію для створення і друку словника, в якому ключі -
# цілі числа від 1 до n включно, а значення - квадрати цих чисел.
# Вхідні дані:
# 10
# Вихідні дані:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

def create_square_dict(n: int):
    square_dict = dict.fromkeys(range(1, n+1), None)
    for key in square_dict:
        square_dict[key] = key ** 2
    return square_dict


print(create_square_dict(10))