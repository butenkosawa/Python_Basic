# Напишіть функцію, яка перевіряє, чи рядок є паліндром чи ні.
# Регістр літер, пропуски і знаки пунктуації не враховувати.
# Примітка. Паліндром - це слово, фраза або послідовність,
# яка читається так само як зліва направо, так і справа наліво.
# Вхідні дані:
# Level
# No 'x' in Nixon
# "Was it a car or a cat I saw?"
# A man, a plan, a canal, Panama!
# palindrome
# Вихідні дані:
# True
# True
# True
# True
# False


def if_palindrom(text: str):
    text = "".join(list(filter(lambda x: x.isalpha(), list(text)))).upper()
    return text == text[::-1]


print(if_palindrom("No 'x' in Nixon"))