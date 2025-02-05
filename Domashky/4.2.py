lst = [1, 3, 5, 10]

if len(lst) > 0:
    result = sum(lst[::2]) * lst.pop()
else:
    result = len(lst)

print(result)
