# Напишіть функцію, яка приймає слово у нижньому регістрі і повертає
# слово з першою великою буквою. Введіть рядок слів через пропуск у
# нижньому регістрі і застосуйте створену функцію для отримання
# результату як у вихідних даних.
# Вхідні дані:
# jived fox nymph grabs quick waltz
# Вихідні дані:
# Jived Fox Nymph Grabs Quick Waltz

def capitalise_word(word: str):
    return word.capitalize()

def capitalise_sentence(sentence: str):
    words = sentence.split()
    capitalise_words = [capitalise_word(word) for word in words]
    return " ".join(capitalise_words)

text = "jived fox nymph grabs quick waltz"
print(capitalise_sentence(text))

