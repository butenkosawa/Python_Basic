# Напишіть функцію, яка перевіряє, чи існує трикутник із введеними сторонами a, b, c.
# Вхідні дані:
# 2 2 1
# 1 2 4
# Вихідні дані:
# True
# False

def is_triangle(a, b, c):
    return all([a + b > c, a + c > b, b + c > a])

print(is_triangle(2, 2, 1))
print(is_triangle(1, 2, 4))