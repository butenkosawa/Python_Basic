# Написати програму, яка переміщає всі нулі у кінець списку. Ваше завдання —
# змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!
#
# Приклад:
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
#
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

lst = [1, 0, 13, 0, 0, 0, 5]
print(lst)

i = 1

while i <= lst.count(0):
    lst.remove(0)
    lst.append(0)
    i += 1

print(lst)

# Рішення викладача

input_list = [1, 0, 13, 0, 0, 0, 5]
# lst = [0]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print("Origin list: ", input_list)

zero_qty = input_list.count(0)
while zero_qty > 0:
    input_list.remove(0)
    input_list.append(0)
    zero_qty -= 1
print("Modified list: ", input_list)