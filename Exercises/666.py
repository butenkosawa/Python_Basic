# Напишіть функцію для сортування рядка слів,
# розділених пропусками, за довжиною слів в порядку зростання.
# Вхідні дані:
# Ruby Python Go JavaScript Java
# Вихідні дані:
# Go Java Ruby Python JavaScript

def sort_string(text: str):
    return ' '.join(sorted(text.split(), key= lambda x: (len(x), x)))


print(sort_string('Java Python Ruby Go JavaScript'))