import random

lst = [random.randint(0,99) for _ in range(random.randint(3,10))]
lst_1 = [lst[0], lst[2], lst[-2]]

print(lst)
print(lst_1)
