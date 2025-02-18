# На вхід функції correct_sentence передається два речення. Необхідно
# повернути їх виправлену копію так, щоб вони завжди починалися з великої
# літери та закінчувалися крапкою. Зверніть увагу, що не всі виправлення
# необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не
# потрібно, це буде помилкою
#
# Вхідні аргументи: string.
# Вихідні аргументи: string.
#
#
# Замість pass необхідно написати Ваше рішення.
# def correct_sentence(text):
#      pass
#
#
# correct_sentence("greetings, friends") -> "Greetings, friends."
# correct_sentence("hello") -> "Hello."
# correct_sentence("Greetings. Friends") -> "Greetings. Friends."
# correct_sentence("Greetings, friends.") -> "Greetings, friends."
# correct_sentence("greetings, friends.") -> "Greetings, friends."
# Не працює з двома реченнями
# correct_sentence("функція має повернути фядок. замініть pass на Ваше рішення.")

def correct_sentence(text):
    if text[-1] != ".":
        text = text + "."
    text = text.split()
    text[0] = text[0].title()
    return " ".join(text)


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))