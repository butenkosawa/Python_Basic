# Дано натуральне ціле додатнє число n. Визначити кількість цифр в ньому.

n = 234
count_dig = 0

while n > 0:
    n = n // 10
    count_dig += 1

print(count_dig)
