lst = [1, 3, 5, 10]

if len(lst) > 0:
    result = sum(lst[::2]) * lst[-1]
else:
    result = len(lst)

print(result)
