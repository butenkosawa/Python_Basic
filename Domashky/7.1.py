# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.
#
# Замініть pass на Ваше рішення.
# def say_hi(name, age):
#   pass
#
#
# say_hi("Alex", 32) -> "Hi. My name is Alex and I'm 32 years old"
# say_hi("Frank", 68) -> "Hi. My name is Frank and I'm 68 years old"

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


print(say_hi("Alex", 32))
print(say_hi("Frank", 68))

# Рішення викладача

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


result = say_hi("Alex", 32)

print(result)