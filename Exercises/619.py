# Напишіть функцію для перевірки того, чи введена літера є голосною чи приголосною.
# Вхідні дані:
# c
# e
# Вихідні дані:
# False
# True

def is_vowel(char):
    return char.upper() in 'AEIOU'


print(is_vowel('c'))
print(is_vowel('e'))
print(is_vowel('o'))