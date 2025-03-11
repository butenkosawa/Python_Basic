# Дана послідовність слів. Написати функцію, яка повертає послідовність
# слів, в якій у словах довжини 3 всі літери великі, а всі слова, що
# починаються на "q" або "f" виключені. Використовувати ланцюжки.
# Приклад: ["The", "quick", "brown", "fox"] -> ["THE", "brown"]

def seq_words(words: list):
    drop_qf = filter(lambda w: not w.startswith(('q','f')), words)
    return list(map(lambda w: w.upper() if len(w)==3 else w, drop_qf))


print(seq_words(["The", "quick", "brown", "fox"]))