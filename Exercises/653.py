# Напишіть функцію, яка приймає два списки та повертає True,
# якщо у них є щонайменше один спільний елемент.
# Вхідні дані:
# 1 2 3 4 5
# 6 7 8 9 0
# 1 two three four five 6 seven 8 9 ten
# five hundred
# Вихідні дані:
# False
# True

def common_element(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    common_set = set1.intersection(set2)
    return len(common_set) > 0


lst1 = [1, 2, 3, 4, 5,]
lst2 = [6, 7, 8, 9, 0]
lst3 = [1, 'two', 'three', 'four', 'five', 6, 'seven', 8, 9, 'ten']
lst4 = ['five', 'hundred']

print(common_element(lst1, lst2))
print(common_element(lst3, lst4))