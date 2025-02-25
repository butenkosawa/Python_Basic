# Використайте словник для виведення представлення букви, яку вводить користувач,
# у символах азбуки Морзе. Передбачте у програмі обробку малих і великих букв.
# Вхідні дані:
# D
# f
# Вихідні дані:
# -..
# ..-.

morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
              'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
              'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..'}

print(morse_dict[input("Enter letter: ").lower()])
