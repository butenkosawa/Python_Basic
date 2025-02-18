# Визначте, скільки різних слів у введеному рядку.

str = 'Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend'
text = str.split()
words = []

for word in text:
    if word not in words:
       words.append(word)

print(len(text))
print(len(words))
