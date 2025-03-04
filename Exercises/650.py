# Напишіть функцію для підрахунку входжень кожного слова в певному реченні.
# Вхідні дані:
# the quick brown fox jumps over the lazy dog
# Вихідні дані:
# {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

def count_words(text: str):
    text = text.split()
    text_dict = dict.fromkeys(text, 0)
    for word in text:
        text_dict[word] += 1
    return text_dict

print(count_words("the quick brown fox jumps over the lazy dog"))