# Напишіть функцію для сортування рядка слів,
# розділених пропусками, за довжиною слів в порядку зменшення.
# Вхідні дані:
# Ruby Python Go JavaScript Java
# Вихідні дані:
# JavaScript Python Java Ruby Go

def sort_string_rev(text: str):
    return ' '.join(sorted(text.split(), key= len, reverse= True))


print(sort_string_rev('Java Python Ruby Go JavaScript'))