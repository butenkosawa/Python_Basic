from random import randint

n = randint(1, 9)

print('+___ ' * n)
print("".join([f'|{i} / ' for i in range(1, n+1)]))
print('|__\\ ' * n)
print('|    ' *n)