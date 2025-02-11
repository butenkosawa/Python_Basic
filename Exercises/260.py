# Дано цілі числа a і b. Обчислити a**b, не використовуючи операцію піднесення до степеня.

a = 2
b = 10

square = 1

for _ in range(b):
   square *= a

print(square)
