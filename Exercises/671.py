# Напишіть функцію для обчислення факторіала заданого числа.
# Вхідні дані:
# 5
# Вихідні дані:
# 120

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

print(factorial(10))