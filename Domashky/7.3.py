# Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти
# індекс другого входження шуканого рядка у рядку для пошуку.
#
# Розберемо перший приклад, де необхідно знайти друге входження "s" в слові
# "sims". Якби нам треба було знайти її перше входження, то тут все просто:
# за допомогою функції index або find ми можемо дізнатися, що "s" - це перший
# символ у слові "sims", а значить індекс першого входження дорівнює 0. Але
# нам Необхідно визначити другу "s", а вона четверта за рахунком. Значить
# індекс другого входження (і у відповідь питання) дорівнює 3.
# Рядок, який потрібно знайти, може складатися з кількох символів.
#
# Input: Два рядки (String).
# Output: Int or None
#
#
# Приклади:
# def second_index(text, some_str):
#   pass
#
#
# second_index("sims", "s") -> 3
# second_index("find the river", "e") -> 12
# second_index("hi", "H") -> None
# second_index("Hello, hello", "lo") -> 10

def second_index(text, some_str):
    n = text.count(some_str)
    index_str = -1
    for _ in range(n):
        index_str = text.find(some_str, index_str + 1)
    if index_str == -1:
        index_str = None
    print(index_str)

second_index("sims", "s")
second_index("find the river", "e")
second_index("hi", "H")
second_index("Hello, hello", "lo")