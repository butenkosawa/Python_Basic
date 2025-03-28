# Перемістити елемент у списку

lst = [1, 99, 3, True, "Hello", 3.5, 'last element']
print(lst)
if len(lst) != 0:
    lst.insert(0, lst.pop())
print(lst)

# Рішення викладача

input_list = input("Введіть елементи списку через пробіл: ").split()
if len(input_list) > 0:
    input_list.insert(0, input_list[-1])
    del input_list[-1]

print(input_list)