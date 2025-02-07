# Перемістити елемент у списку

lst = [1, 99, 3, True, "Hello", 3.5, 'last element']
print(lst)
if len(lst) != 0:
    lst.insert(0, lst.pop())
print(lst)
