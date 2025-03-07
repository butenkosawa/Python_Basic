# Дано список кортежів, кожен з яких містить два значення:
# назва фільму (рядок) і рейтинг (дійсне число).
# Напишіть функцію(ї) для сортування кортежів в порядку зростання рейтингу.
# Вхідні дані:
# Список із кортежів
# Вихідні дані:
# [('Captain Marvel', 7.0), ('Aladdin', 7.4), ('Toy Story 4', 8.2), ('Avengers: Endgame', 8.7)]

def sort_films(films):
    return sorted(films, key= lambda x: x[-1])

films = [('Toy Story 4', 8.2), ('Aladdin', 7.4),  ('Avengers: Endgame', 8.7), ('Captain Marvel', 7.0)]
print(sort_films(films))