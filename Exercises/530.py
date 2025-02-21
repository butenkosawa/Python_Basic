# Створити словник, у якому ключами є назви команд Національної баскетбольної асоціації (NBA) у північній Америці,
# а значеннями - списки, на зразок, [Всього ігор, Перемог, Нічиїх, Поразок, Всього очок].
# Значення списку - це цілі числа, які обираються довільно.
# Надрукуйте інформацію про кожну команду як у вихідних даних.
# Вхідні дані:
# Немає
# Вихідні дані:
# BOSTON CELTICS 3 2 0 1 8
# NEW YORK KNICKS 10 3 3 4 19
# INDIANA PACERS 4 2 2 0 11
# MIAMI HEAT 12 2 5 5 9
# ATLANTA HAWKS 5 2 2 1 10
# CHICAGO BULLS 25 10 9 6 38

from random import randint

commands = ("BOSTON CELTICS", "NEW YORK KNICKS", "INDIANA PACERS", "MIAMI HEAT", "ATLANTA HAWKS", "CHICAGO BULLS")
statist = []
games = randint(0,72)

for _ in range(len(commands)):
    scores = []
    scores.append(games)
    scores.append(randint(0,scores[0]))
    scores.append(randint(0, scores[0] - scores[1]))
    scores.append(scores[0] - sum(scores[1:]))
    scores.append(scores[1] * 3 + scores[2])
    statist.append(scores)

nba = dict(zip(commands, statist))

for key, values in nba.items():
    print(key, end=" ")
    for value in values:
        print(value, end=" ")
    print()


