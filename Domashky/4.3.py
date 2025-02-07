import random

len_lst = random.randint(3,10)
lst = []

for lst_elem in range(len_lst):
    lst.append(random.randint(0,99))

lst_1 = [lst[0], lst[2], lst[-2]]

print(lst)
print(lst_1)
