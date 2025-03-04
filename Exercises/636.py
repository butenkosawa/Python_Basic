# Напишіть програму, і створіть в ній дві функції.
# Перша з них - приймає послідовність цілих чисел і повертає список.
# Друга - повертає новий список, що містить всі елементи першого списку без дублікатів.
# Вхідні дані:
# 5 16 5 29 11 217 11
# Вихідні дані:
# [5, 11, 16, 217, 29]

def create_list(*args):
    return list(args)

def remove_duplicates(lst):
    return list(set(lst))


numbers = create_list(5, 16, 5, 29, 11, 217, 11)
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)