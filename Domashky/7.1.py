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
    print(f"Hi. My name is {name} and I'm {age} years old")


say_hi("Alex", 32)
say_hi("Frank", 68)