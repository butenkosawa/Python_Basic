# Напишіть функцію, щоб вилучити певні символи із введеного рядка.
# Спочатку вводиться початковий рядок, а далі з нового рядка символи,
# які необхідно вилучити з початкового рядка.
# Результатом має бути новий рядок без вилучених символів.
# Вхідні дані:
# I did, did I?
# d?
# Вихідні дані:
# I i, i I

def remove_char(text: str, char_for_del: str):
    for char in text:
        if char in char_for_del:
            text = text.replace(char, '')
    return text


text1 = "I did, did I?"
char_for_del1 = "d?"

print(text1)
print(remove_char(text1, char_for_del1))