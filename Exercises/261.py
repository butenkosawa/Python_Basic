# Напишіть програму, яка зчитує числа (по одному в рядку) до тих пір,
# поки сума введених чисел не буде дорівнювати 0 і відразу після цього
# виводить суму квадратів всіх введених чисел. Гарантується, що в якийсь момент
# сума введених чисел дорівнюватиме 0, після цього зчитування продовжувати не потрібно.

summ = 0
summ_sq = 0

while True:
    n = int(input("Enter number n: "))
    summ += n
    summ_sq += n ** 2
    if summ == 0:
        break

print(summ_sq)