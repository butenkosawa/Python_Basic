# Напишіть генератор, який генеруватиме нескінченну послідовність Фібоначчі.
# Щоразу, коли генератор викликається, він повинен повертати таку кількість
# послідовності. Напишіть програму, яка використовуватиме цей генератор для
# виведення перших N чисел Фібоначчі.
# Приклад висновку:
# Введіть кількість чисел Фібоначчі: 10
# Перші 10 чисел Фібоначчі:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a

n = 20
fib = fib_gen()

while n > 0:
    print(next(fib))
    n -= 1
