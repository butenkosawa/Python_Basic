# Напишіть функцію, яка отримує рядок і ціле число n та повертає n копій заданого рядка.
# Вхідні дані:
# I love coding
# 3
# Вихідні дані:
# I love codingI love codingI love coding

def multy_string(string, n):
    return string * n


print(multy_string("I love coding", 3))