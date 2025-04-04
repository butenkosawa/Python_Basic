# Надрукуйте найменше з трьох введених чисел без використання вбудованої функції min().
# Для цього напишіть першу функцію, яка повертає найменше число з двох заданих.
# У другій функції реалізуйте використання першої функції
# для визначення найменшого значення серед трьох чисел.
# Вхідні дані:
# 5 8 11
# 12 12 24
# 1 1 1
# Вихідні дані:
# 5
# 12
# 1

def min_of_two(a, b):
    return a if a < b else b

def min_of_three(a, b, c):
    return min_of_two(min_of_two(a, b), c)

# Вхідні дані
inputs = [
    (5, 8, 11),
    (12, 12, 24),
    (1, 1, 1)
]

# Обробка та вивід результатів
for a, b, c in inputs:
    print(min_of_three(a, b, c))
