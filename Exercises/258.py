# Для обчислення числа Пі можна використовувати наступне наближення (ряд Лейбніца):
# Pi = 4/1 - 4/3 + 4/5 - 4/7 + .... Обчисліть перші n членів цього ряду.

n = int(input("Enter n: "))
pi = 0

for i in range(n):
    pi += ((-1) ** i) * (4 / (2 * i + 1))

print(pi)

# ------------------------------------------

lst_divider = list(range(1, 2*n+1, 2))
pi = 0

for itr, el in enumerate(lst_divider, 1):
    if itr % 2 == 0:
        pi -= 4 / el
        continue
    pi += 4 / el

print(pi)

# ------------------------------------------

pi = 0

for i in range(1, 2*n+1, 2):
    if i in range(1, 2*n+1, 4):
        pi += 4 / i
    elif i in range(3, 2*n+1, 4):
        pi -= 4 / i

print(pi)
