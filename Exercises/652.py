# Напишіть функцію, яка друкує усі слова із списку, довжина яких перевищує n.
# Вхідні дані:
# Denmark England Estonia France Greece Romania Ukraine
# 6
# Вихідні дані:
# Denmark England Estonia Romania Ukraine

def wordslenprint(words: list, n: int):
    for word in list(filter(lambda x: len(x) > n, words)):
        print(word, end=" ")

wordslenprint(['Denmark', 'England', 'Estonia', 'France', 'Greece', 'Romania', 'Ukraine'], 6)