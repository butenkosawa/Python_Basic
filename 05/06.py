string_1 = "I like Python so much"
string_2 = "Python"
string_3 = "123456"
string_4 = "1234sdf569asd!"

print(string_1.find('i'))
print(string_1.find('o'))
print(string_1.find('o', 12))
print(string_1.count('o',2,12))

ind = string_1.find('o')
print(ind)
ind = string_1.find('o', ind+1)
print(ind)

print(string_1.isalpha())
print(string_2.isalpha())

print(string_3.isdigit())
print(string_4.isalnum())