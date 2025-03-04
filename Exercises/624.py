# Напишіть функцію для вставки рядка всередину іншого рядка.
# Вхідні дані:
# [] Python
# <<>> HTML
# qwerty 123
# Вихідні дані:
# [Python]
# <<HTML>>
# qwe123rty

def string_in_midstring(str1, str2):
    mid = int(len(str1) / 2)
    return str1[:mid] + str2 + str1[mid:]

print(string_in_midstring('[]', 'Python'))
print(string_in_midstring('<<>>', 'HTML'))
print(string_in_midstring('qwerty', '123'))
