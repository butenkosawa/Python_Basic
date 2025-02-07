# Напишіть програму, яка приймає ціле число n
# і обчислює значення виразу n + nn + nnn

num = input('Введіть ціле число, n = ')

n = int(num)
nn = int(num * 2)
nnn = int(num * 3)

print('n + nn + nnn =', n + nn + nnn)
