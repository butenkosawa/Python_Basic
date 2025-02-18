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

def correct_sentence(text):
    text = text.strip()
    dots = text.count(".")

    if dots == 0:
        text = text.split()
        text[0] = text[0].title()
        correct_text = " ".join(text) + "."

    elif dots == 1:
        if text.index('.') == 0 or text.index('.') == len(text) - 1:
            text = text.replace('.', '') + '.'
            text = text.split()
            text[0] = text[0].title()
            correct_text = " ".join(text)
        else:
            dot_index = text.index(".")
            text_1 = text[:dot_index + 1].split()
            text_1[0] = text_1[0].title()
            text_2 = (text[dot_index + 1:].strip() + ".").split()
            text_2[0] = text_2[0].title()
            correct_text = " ".join(text_1) + " " + " ".join(text_2)

    else:
        dot_index_1 = text.index(".")
        dot_index_2 = text.index(".",  dot_index_1+1)
        if dot_index_1 != 0:
            text_1 = text[:dot_index_1 + 1].split()
            text_1[0] = text_1[0].title()
            if dot_index_2 == len(text) - 1:
                text_2 = text[dot_index_1 + 1:].strip().split()
                text_2[0] = text_2[0].title()
            else:
                text_2 = text[dot_index_1 + 1:dot_index_2 + 1].strip().split()
                text_2[0] = text_2[0].title()

        # text_1 = text[:dot_index_1 + 1].split()
        # text_1[0] = text_1[0].title()
        # text_2 = text[dot_index_1 + 1:].strip().split()
        # text_2[0] = text_2[0].title()


        correct_text = " ".join(text_1) + " " + " ".join(text_2)


    print(correct_text)


correct_sentence("функція має повернути фядок. замініть pass на Ваше рішення.")
correct_sentence("greetings, friends")# -> "Greetings, friends."
correct_sentence("hello")#  -> "Hello."
correct_sentence("Greetings. Friends")#  -> "Greetings. Friends."
correct_sentence("Greetings, friends.")#  -> "Greetings, friends."
correct_sentence("greetings, friends.")# -> "Greetings, friends."
#


