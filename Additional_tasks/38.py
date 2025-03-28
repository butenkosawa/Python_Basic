# Дана послідовність слів. Написати функцію, яка повертає послідовність
# слів з вихідної послідовності відсортованих по алфавіту, довжина
# яких більше трьох букв і до кожного слова застосовано метод title().
#
# Приклад: ["HellO", "WORLD", "names", "Is", "Sam", "NO", "apple"]
# Результат: ['Apple', 'Hello', 'Names', 'World']

def sorted_words(words: list):
    words = sorted(list(map(lambda x: x.title(), words)))
    return list(filter(lambda x: len(x) > 3, words))


print(sorted_words(["HellO", "WORLD", "names", "Is", "Sam", "NO", "apple"]))

# Рішення викладача:

def func(list_str):
    return sorted(filter(lambda x: len(x) > 3, map(str.title, list_str)))


strings = ["HellO", "WORLD", "names", "Is", "Sam", "NO", "apple"]
print(func(strings))