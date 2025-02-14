# Напишіть програму, яка зчитує рядок, введений користувачем, та визначає у ньому: кількість великих літер, кількість малих літер, кількість символів пропуску.
# Вхідні дані:
# By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name.
# Вихідні дані:
# Upper 4
# Lower 76
# Spaces 18

txt = "By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name."
upper = 0
lower = 0
spaces = 0

for sym in txt:
    if sym.isupper():
        upper += 1
    elif sym.islower():
        lower += 1
    elif sym == ' ':
        spaces += 1
    else:
        continue

print('Upper:', upper)
print('Lower:', lower)
print('Spaces:', spaces)
