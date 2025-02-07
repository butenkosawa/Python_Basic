lst = [1, 0, 13, 0, 0, 0, 5]
print(lst)

i = 1

while i <= lst.count(0):
    lst.remove(0)
    lst.append(0)
    i += 1

print(lst)
