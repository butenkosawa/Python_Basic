# Напишіть програму, яка знайде максимально можливе число, яке можна отримати після видалення однієї цифри.
# Перший рядок містить одне ціле число n (10 ≤ n ≤ 2025). Виведіть у другому рядку максимально можливе число,
# яке можна отримати після видалення однієї цифри.
# Вхідні дані:
# 4378
# 1095
# 2000
# Вихідні дані:
# 478
# 195
# 200

nmbr = tuple(str(3698652))
print(nmbr)
nmbrs = []

for i in range(len(nmbr)):
    n = list(nmbr)
    del n[i]
    nmbrs.append(int(''.join(n)))

print(max(nmbrs))