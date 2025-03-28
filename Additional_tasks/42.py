# Дана послідовність слів. Написати функцію, яка повертає послідовність
# слів, в якій у словах довжини 3 всі літери великі, а всі слова, що
# починаються на "q" або "f" виключені. Використовувати ланцюжки.
# Приклад: ["The", "quick", "brown", "fox"] -> ["THE", "brown"]

def seq_words(words: list):
    drop_qf = filter(lambda w: not w.startswith(('q','f')), words)
    return list(map(lambda w: w.upper() if len(w)==3 else w, drop_qf))


print(seq_words(["The", "quick", "brown", "fox"]))

# Рішення викладача:

def funk2(words_list):
    return map(lambda x: x.upper() if len(x) == 3 else x, filter(lambda x: not x.startswith(('q', 'f')), words_list))


words = ["The", "quick", "brown", "fox"]

print(list(funk2(words)))