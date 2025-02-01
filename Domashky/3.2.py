# Перемістити елемент у списку

lst = [1, 99, 3, True, "Hello", 3.5, 'last element']
# lst = ['Bob']
# lst = []

print(lst)

a = len(lst)

if a != 0:
    last_elm = lst.pop()
    # print(last_elm)
    # print(lst)
    lst.insert(0, last_elm)

print(lst)
