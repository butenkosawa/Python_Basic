# Дано три цілих числа. Визначте, скільки серед них збігаються.
# Програма повинна вивести одне з чисел:
# 3 (якщо усі однакові), 2 (якщо два однакові) або 0 (якщо усі числа різні).

num1 = 1
num2 = 5
num3 = 2

if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num2 == num3 or num1 == num3:
    print(2)
else:
    print(0)
