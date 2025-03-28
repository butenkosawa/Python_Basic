# Даний список, що складається з даних різного типу.
# Повернути новий список, де за допомогою функції map() кожен елемент типу
# int початкового списку приведений до типу str, елементи решти всіх типів
# передаються в новий список без зміни їх типу.
# У якості вхідної функції в map використовувати lambda-функцію.

data = [1, 'kilo', 3, False, 2.1,  None, [1269, 'Hello'], 100]
updata = list(map(lambda x: str(x) if isinstance(x, int) else x, data))
updata2 = list(map(lambda x: str(x) if type(x) is int else x, data))

print(data)
print(updata)
print(updata2)

# Рішення викладача:

values = [1, 2, '3', 'forth', 'end', 99, True, None]
new_value = list(map(lambda x: str(x) if type(x) is int else x, values))
print(new_value)