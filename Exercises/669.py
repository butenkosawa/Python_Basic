# Напишіть функцію, яка створює комбінацію
# двох послідовностей таким чином як у вихідних даних.
# Вхідні дані:
# 1 2 3 4 5
# a b c d e
# Вихідні дані:
# 1 a 2 b 3 c 4 d 5 e

def combine_sequences(seq1, seq2):
    combined = []
    for a, b in zip(seq1.split(), seq2.split()):
         combined.append(a)
         combined.append(b)
    return " ".join(combined)


seq1 = "1 2 3 4 5"
seq2 = "a b c d e"

print(combine_sequences(seq1, seq2))