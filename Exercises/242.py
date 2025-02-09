# Дано два цілих числа a і b. Виведіть всі числа від a до b включно, в порядку зростання,
# якщо a < b, або в порядку спадання у іншому випадку.

a = 12
b = 1

if a < b:
    for i in range(a, b+1):
        print(i, end=' ')
else:
    for i in range(a, b-1, -1):
        print(i, end=' ')

# while a >= b:
#     print(a, end=' ')
#     a -= 1
# # while a <= b:
#     print(a, end=' ')
#     a += 1
