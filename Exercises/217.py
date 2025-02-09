# Надрукувати всі цілі числа від a до b включно, кратні деякому числу c.
# Числа a, b, c - цілі числа, які вводить користувач.
# Вхідні дані:
# 20
# 50
# 3
# Вихідні дані:
# 21 24 27 30 33 36 39 42 45 48

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

for num in range (a, b + 1):
    if num % c == 0:
        print (num, end=' ')
