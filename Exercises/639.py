# Напишіть функцію, яка об’єднує всі елементи послідовності, введені через пропуск,
# в рядок, де елементи вже розділені комою і одним пропуском, і повертає його як у вихідних даних.
# Вхідні дані:
# Python Ruby C Go Java JavaScript
# Вихідні дані:
# Python, Ruby, C, Go, Java, JavaScript

def sep_by_coma(sequence):
    sequence_list = sequence.split()
    sequence_list = list(map(lambda x: x + ',', sequence_list))
    return " ".join(sequence_list).strip(',')   # (" ".join(list(map(lambda x: x + ',', sequence.split())))).strip(',')

print(sep_by_coma('Python Ruby C Go Java JavaScript'))