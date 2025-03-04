# Напишіть програму, яка приймає список слів і повертає список, містить тільки
# анаграми. Анаграми - це слова, складені з тих самих букв, але у різному
# порядку. Створіть функцію anagrams, яка приймає список слів як аргумент
# та повертає список анаграм. Використовуйте безліч і сортування букв у слові
# для перевірки на анаграму. Виведіть результат на екран.
#
# Приклад переданого списку слів:
# ['cat', 'dog', 'tac', 'god', 'act']
#
# Приклад висновку:
# Анаграми: ['dog', 'god'], ['cat', 'tac', 'act']

def anagrams(word_list) -> list:
    sorted_by_letters = set(map(lambda word: "".join(sorted(word)), word_list))
    anagrams_dict = {key: [] for key in sorted_by_letters}

    for word in word_list:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]

    result = [value for value in anagrams_dict.values()]

    return sorted(result, key = lambda x: len(x))


print(anagrams(['cat', 'dog', 'tac', 'god', 'act']))
