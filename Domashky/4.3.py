# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до
# 10. Ваше завдання - створити новий список з 3 елементів початкового списку -
# першим, третім і другим з кінця.
#
# Приклад:
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

import random

lst = [random.randint(0,99) for _ in range(random.randint(3,10))]
lst_1 = [lst[0], lst[2], lst[-2]]

print(lst)
print(lst_1)

# Рішення викладача

lst = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print("Origin list: ", lst)
new_lst = [lst[0], lst[2], lst[-2]]
print("Modified list: ", new_lst)
