# Напишіть програму для підрахунку кількості символів (символьної частоти) у введеному рядку.
# Вхідні дані:
# google
# Вихідні дані:
# g 2
# o 2
# l 1
# e 1
from collections import defaultdict

text = 'google'
chars = {}

for char in text:
    chars[char] = chars.get(char, 0) + 1

for k, v in chars.items():
    print(k, v)

