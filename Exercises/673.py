# Напишіть функцію для перевірки, чи є даний рядок анаграмою іншого рядка.
# Букви початкового рядка використовуються одноразово і враховується регістр літер.
# Примітка. Анаграма - переставлення літер у слові, завдяки чому утворюється нове значення слова.
# Вхідні дані:
# eleven plus two
# twelve plus one
# I am Lord Voldemort
# tom marVoLo rIddle
# Forty five
# over fifty
# Вихідні дані:
# True
# True
# False

def is_anagramm(text1: str, text2: str):
    print(text1)
    print(text2)
    text1 = sorted(''.join(filter(lambda x: x.isalpha(), text1)))
    text2 = sorted(''.join(filter(lambda x: x.isalpha(), text2)))
    print(text1)
    print(text2)
    return text1 == text2

t1 = 'eleven plus two'
t2 = 'twelve plus one'
print(is_anagramm(t1, t2))
print('-' * 30)
t1 = 'I am Lord Voldemort'
t2 = 'tom marVoLo rIddle'
print(is_anagramm(t1, t2))
print('-' * 30)
t1 = 'Forty five'
t2 = 'over fifty'
print(is_anagramm(t1, t2))
