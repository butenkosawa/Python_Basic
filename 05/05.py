string_1 = "     I like PHP, PHP, PHP,  "
string_2 = string_1.strip('I ,PH')
string_3 = string_1.lstrip('I ,PH')
string_4 = string_1.rstrip('I ,PH')

print(string_1)
print(string_2)
print(string_3)
print(string_4)