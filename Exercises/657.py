# Дано дійсне додатне число a і ціле число n, яке може набувати додатних
# і від’ємних значень. Напишіть функцію для обчислення a**n.
# Стандартною функцією піднесення до степеня і оператором ** користуватися не можна.
# Вхідні дані:
# 2
# 1
# 2
# -1
# Вихідні дані:
# 2.0
# 0.5

def power_number(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / a * power_number(a, n + 1)
    return a * power_number(a, n - 1)


print(power_number(2, 10))
print(power_number(2, -1))