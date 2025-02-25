# На вхід функції popular_words передаються два аргументи. Текст та список слів,
# популярність яких необхідно визначити. При вирішенні цього завдання зверніть
# увагу на такі моменти. Слова необхідно шукати у всіх регістрах. Тобто. якщо
# необхідно знайти слово "one", значить для нього будуть підходити слова "one",
# "One", "oNe", "ONE" і т.д. Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі
# значенням 0 (нуль)
# Вхідні параметри: Текст і масив слів, що шукаються.
# Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями,
# скільки разів кожнє слово зустрічаються у орігінальному тексті.
#
# Приклад:
# def popular_words (text, words):
# pass
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
#                      ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
# print('OK')

def popular_words(text: str, searched_words: list):
    from string import punctuation
    count_words = dict.fromkeys(searched_words, 0)
    for el in punctuation:
        text = text.replace(el, "").lower()
    for word in text.split():
        if word in count_words:
            count_words[word] += 1
    return count_words


sentence = 'When I was One I had just begun When I was Two I was nearly new'
words = ['i', 'was', 'three', 'near']

sentence_2 = ('Python is one of the top programming languages in the world, '
              'widely used in fields such as AI, machine learning, '
              'data science, and web development.')
words_2 = ['python', 'in', 'the', 'world', 'ai', 'develop']

print(popular_words(sentence, words))
print(popular_words(sentence_2, words_2))