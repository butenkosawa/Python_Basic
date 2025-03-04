# Напишіть функцію для визначення більшого з двох цілих чисел без використання вбудованої функції max().
# Якщо числа рівні, то вивести повідомлення equal.
# Вхідні дані:
# 12 56
# 11 4
# 3 3
# Вихідні дані:
# 56
# 11
# equal

def larger_number(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return 'equal'


print(larger_number(12, 56))
print(larger_number(11, 4))
print(larger_number(3, 3))
