# Напишіть програму, яка запитує у користувача число N і виводить
# перші N чисел Фібоначчі. Числа Фібоначчі - це послідовність чисел,
# де кожне наступне число є сумою двох попередніх чисел
# (починаючи з 0 та 1). Використовуйте цикл while для розв'язання задачі.
# Виведіть числа через кому за допомогою команди print.
#
# Приклад:
# Введіть число N: 7
# Перші 7 чисел Фібоначчі: 0, 1, 1, 2, 3, 5, 8

n = int(input('Введіть кількість перших чисел Фібоначі, n = '))
fibonachi_list = [0, 1]

while len(fibonachi_list) < n:
    fibonachi_list.append(sum(fibonachi_list[-2:]))

print(f'Перші {n} чисел Фібоначчі:')
print(''.join([str(dg)+', ' for dg in fibonachi_list]).strip(", "))

# Рішення викладача:

N = int(input('Введіть число N:'))
a = 0
print('Перші', N, 'числ Фібоначчі:', end='')
b = 1
count = 2
while count <= N:
    print(a, end=', ')
    c = a + b
    a = b
    b = c
    count += 1
else:
    print(a)