# Напишіть функцію для перевертання кожного слова у введеному тексті.
# Вхідні дані:
# poT tops
# oN ,nomel on nolem
# Вихідні дані:
# Top spot
# No lemon, no melon

def reverse_word(word):
    if len(word) == 0:
        return word
    else:
        return reverse_word(word[1:]) + word[0]

def reverse_words_recursively(sentence):
    words = sentence.split()
    reversed_words = [reverse_word(word) for word in words]
    return ' '.join(reversed_words).capitalize()

input_sentence1 = "poT tops"
input_sentence2 = "oN ,nomel on nolem"

output_sentence1 = reverse_words_recursively(input_sentence1)
output_sentence2 = reverse_words_recursively(input_sentence2)

print(output_sentence1)
print(output_sentence2)


# def revers_words(text):
#     return " ".join(word[::-1] for word in text.split())
#
# print(revers_words('poT tops'))
# print(revers_words('oN ,nomel on nolem'))