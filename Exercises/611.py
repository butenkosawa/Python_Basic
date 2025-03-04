# Напишіть функцію для отримання рядка з перших n символів іншого рядка.
# Якщо довжина рядка менше n, поверніть початковий рядок.
# Вхідні дані:
# 5
# Java
# 2
# Java
# Вихідні дані:
# Java
# Ja

def first_chars(string, n):
    return string if len(string) < n else string[:n]


print(first_chars('Java', 2))
print(first_chars('Java', 5))