string_1 = "I like PHP, PHP, PHP,"
string_2 = string_1.replace('PHP', 'Python').replace(',', '!')
print(string_1)
print(string_2)

string_3 = "I like Python so much"
lst = string_3.split()
print(string_3)
print(lst)

lst_1 = ['I', 'Like', 'Python', '!']
string_4 = ''.join(lst_1)
print(string_4)
print("_".join('I like Python so much'))

lst_2 = [1, 2, 3]
num = ''.join([str(el) for el in lst_2])
print(num)
print(type(num))
