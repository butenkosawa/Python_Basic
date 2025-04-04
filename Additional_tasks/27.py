# Напишіть програму, яка за числом n від 1 до 9 виводить на екран n
# пінгвінів. Зображення одного пінгвіна має розмір 5х9 символів.
# Вхідні дані:
# Вводиться натуральне число.
# Вихідні дані:
# Виводиться введена кількість пінгвінів у рядок.
# Примітка:
# Врахуйте, що виведення даних на екран робиться рядковим, а не попінгвінним.
#
# У деяких мовах програмування символ зворотного слеша “\” у текстових
# рядках має спеціальне значення. Щоб включити до текстового рядка
# такий символ, його потрібно повторити двічі. Наприклад, для виведення на екран
# одного такого символу можна використовувати такий код: print("\\").
#    _~_
#   (o o)
#  /  V  \
# /(  _  )\
#   ^^ ^^
#
# Приклад:
# Введить кількість пінгвінів: 3
#     _~_        _~_        _~_
#    (o o)      (o o)      (o o)
#   /  V  \    /  V  \    /  V  \
#  /(  _  )\  /(  _  )\  /(  _  )\
#    ^^ ^^      ^^ ^^      ^^ ^^
from random import randint

n = randint(1, 9)
print(n)

row1 = '_~_'.center(9) + ' ' * 2
row2 = '(o o)'.center(9) + ' ' * 2
row3 = '/  V  \\'.center(9) + ' ' * 2
row4 = '/(  _  )\\'.center(9) + ' ' * 2
row5 = '^^ ^^'.center(9) + ' ' * 2

print(row1 * n)
print(row2 * n)
print(row3 * n)
print(row4 * n)
print(row5 * n)

# Рішення викладача:

n = int(input("Введите число пингвинов: "))
penguin = ["_~_", "(o o)", "/  V  \\", "/(  _  )\\", "^^ ^^"]
for i in penguin:
    # print(i.center(11) * n)
    print(f"{i:^11}" * n)