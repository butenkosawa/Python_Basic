# Учні 5 класу вели щоденники спостереження за погодою і щодня записували денну температуру.
# Знайдіть найнижчу температуру за весь час спостережень. Якщо температура знижувалась нижче -15 градусів,
# необхідно вивести Yes, у протилежному випадку No. Програма отримує на вхід кількість днів,
# протягом яких проводилося спостереження n (1 ≤ n ≤ 31), потім для кожного дня вводиться температура.

days = int(input("Enter number of days: "))
list_temp = []

for day in range(1, days+1):
    temp = int(input(f"Enter the temperature of {day} day: "))
    list_temp.append(temp)

print(f"Lowest temperature: {min(list_temp)} oC")

if min(list_temp) < -15:
    print("Yes")
else:
    print("No")