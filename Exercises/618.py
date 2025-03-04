# Напишіть функцію, яка до введеного рядка на початку додає рядок Is.
# Якщо даний рядок вже починається з Is, то початковий рядок виводиться без змін.
# Вхідні дані:
# list
# Is empty
# Вихідні дані:
# Is list
# Is empty

def add_word_to_start(string: str, word = 'Is'):
    if string.split()[0] != word:
        return word + ' ' + string
    return string


print(add_word_to_start("list"))
print(add_word_to_start("Is list"))