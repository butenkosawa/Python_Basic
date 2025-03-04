# Напишіть функцію, яка приймає два слова в якості вхідних даних, і надрукуйте найдовше слово.
# Якщо слова мають однакову довжину, то функція повинна надрукувати слова в окремих рядках.
# Вхідні дані:
# five three
# Вихідні дані:
# three

def longer_word(word1, word2):
    if len(word1) > len(word2):
        return word1
    elif len(word1) < len(word2):
        return word2
    else:
        return word1 + '\n' + word2

print(longer_word('five', 'three'))
print('*' * 10)
print(longer_word('five', 'thre'))