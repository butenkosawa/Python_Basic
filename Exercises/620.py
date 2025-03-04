# Напишіть функцію для створення позначок тегів HTML навколо введених рядків.
# Функція отримує назву тега HTML і рядок, який необхідно помістити у відповідні теги.
# Вхідні дані:
# strong Python
# Вихідні дані:
# <strong>Python</strong>

def create_tag_html(tag: str, string: str):
    return '<' + tag + '>' + string + '</' + tag + '>'


print(create_tag_html('strong', 'Python'))