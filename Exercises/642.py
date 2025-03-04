# Напишіть функцію, яка приймає послідовність слів,
# розділених за допомогою дефісу і друкує слова в послідовності,
# розділеній за допомогою дефісу, після сортування за алфавітом.
# Вхідні дані:
# one-two-three-four-five-six-seven
# Вихідні дані:
# five-four-one-seven-six-three-two

def sort_by_alphabet(sequence: str):
    sequence_lst = sorted(sequence.split('-'))
    return '-'.join(sequence_lst)


print(sort_by_alphabet('one-two-three-four-five-six-seven'))