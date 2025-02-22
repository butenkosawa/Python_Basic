# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок
# паліндромом. Паліндромом - це такий рядок, який читається однаково зліва
# направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
#
# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# print("ОК")

def is_palindrome(text):
    punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    for el in text:
        if el in punctuation:
            text = text.replace(el, "").lower()
    return text == text[-1::-1]


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))