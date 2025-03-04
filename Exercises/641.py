# Напишіть функцію для перевірки наявності одного списку у іншому списку.
# Cписки містять принаймні по одному елементу.
# Вхідні дані:
# 2 6 8 4 9 1
# 4 9
# 2 6 8 4 9 1
# 9 4
# Вихідні дані:
# True
# False

def if_list_in_list(lst1, lst2):
    str1 = ''.join(list(map(lambda x: str(x) ,lst1)))
    str2 = ''.join(list(map(lambda x: str(x) ,lst2)))
    if len(str1) > len(str2):
        return str2 in str1
    elif len(str2) > len(str1):
        return str1 in str2

print(if_list_in_list([2, 6, 8, 4, 9, 1], [4, 9]))
print(if_list_in_list([2, 6, 8, 4, 9, 1], [9, 4]))