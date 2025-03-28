# Напишіть функцію is_subset, яка приймає дві множини set1 і set2 і
# перевіряє, чи є set1 підмножиною set2. Функція має повертати
# True, якщо всі елементи set1 містяться в set2, і False в іншому
# Випадок. Функція має бути реалізована без використання вбудованих методів
# issubset або <=.
#
# Приклад множин
# {1, 2, 3}
# {1, 2, 3, 4, 5}
#
# Приклад висновку:
# True

def is_subset(set1, set2):
    for el in set1:
        if el not in set2:
            return False
    return True

print(is_subset({1, 2, 3}, {1, 2, 3, 4, 5}))

# Рішення викладача:

def is_subset(s1, s2):
    p = True
    for i in s1:
        if i not in s2:
            p = False
            break
    return p


set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(is_subset(set1, set2))