# Напишіть функцію, яка отримує рядок слів, розділених пропуском.
# Надрукуйте рядок слів у звороному порядку.
# Вхідні дані:
# one two three
# Вихідні дані:
# three two one

def reverse_words_in_string(string: str):
    return ' '.join(string.split()[::-1])


print(reverse_words_in_string('one two three'))