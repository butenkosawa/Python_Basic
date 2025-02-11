name = 'Oleksandr'
age = 23

tmpl = 'My name is {}. I am {} yeas old.'
tmpl_2 = 'My name is {0}. I am {1} yeas old. I was born {1} years ago :)'
tmpl_3 = 'My name is {name}. I am {age} yeas old. I was born {age} years ago :)'
text_1 = tmpl.format('Maria', 18)
text_2 = tmpl_2.format('Maria', 18)
text_3 = tmpl.format(name, age)
text_4 = tmpl_3.format(name = name, age = age)
text_5 = tmpl_3.format(name = 'Vova', age = 89)
print(text_1)
print(text_2)
print(text_3)
print(text_4)
print(text_5)