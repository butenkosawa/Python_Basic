# Напишіть функцію find_longest_word, яка прийматиме список слів і
# повертати найдовше слово зі списку.
# Анотуйте типи аргументів і значення функції, що повертається.
#
# Приклад виклику функції та очікуваного виводу:
# words = ["apple", "banana", "cherry", "dragonfruit"]
# result = find_longest_word(words)
# print(result)
# Очікуваний висновок: "dragonfruit"

def find_longest_word(words: list):
    return sorted(words, key=len)[-1]

w = ["apple", "banana", "cherry", "dragonfruit"]
print(find_longest_word(w))

