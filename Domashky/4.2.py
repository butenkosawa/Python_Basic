lst = [1, 3, 5, 10]
print(sum(lst[::2]) * lst[-1] if len(lst) > 0 else len(lst))
