# Напишіть функцію, яка отримує рядок і обчислює кількість великих та нижніх букв
# в ньому і друкує результат як у вихідних даних - спочатку кількість великих,
# а потім кількість малих літер.
# Вхідні дані:
# Was it a car or a cat I saw?
# Вихідні дані:
# 2
# 17

def count_letters(text: str):
    count_upper = 0
    count_lower = 0

    for char in text:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        else:
            continue

    return f'Upper letters: {count_upper}\nLower letters: {count_lower}'

print(count_letters('Was it a car or a cat I saw?'))