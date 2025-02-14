# Напишіть програму для отримання рядка Фібоначчі від 0 до n, де n - ціле число.
# Послідовність Фібоначчі - це серія чисел 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Кожне наступне число знайдено шляхом додавання двох номерів перед ним.

n = 500
fibonachi = [0, 1]

while True:
    fibonachi.append(sum(fibonachi[-2:]))
    if fibonachi[-1] > n:
        fibonachi.pop()
        break

for dg in fibonachi:
    print (dg, end=' ')
