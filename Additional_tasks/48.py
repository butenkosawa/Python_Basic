# Створіть власний клас String на основі стандартного класу str.
# В ньому необхідно:
#      • Розширити стандартний метод, відповідальний за додавання
#      • Написати відсутній у класі str метод відповідальний за віднімання
#
# Принцип роботи в новому класі String: об'єкти типу String можна додавати як
# між собою, так і з будь-яким іншим типом, який може бути приведений до типу
# рядка. "Під капотом", обидва операнди приводиться до типу рядків та потім
# відбувається конкаткатенація. Результатом додавання буде новий об'єкт класу
# String. Приклади виконання:
#
# String('New') + String(890)    ->    'New890'
# String(1234) + 5678            ->    '12345678'
# String('New') + 'castle'       ->    'Newcastle'
# String('New') + 77             ->    'New77'
# String('New') + True           ->    'NewTrue'
# String('New') + ['s', ' ', 23] ->    "New['s', ' ', 23]"
# String('New') + None           ->    'NewNone'
#
# Принцип віднімання в новому класі String: з об'єкту типу String ви можете
# відняти значення будь-якого іншого типу, яке можна привести до типу рядка.
# "Під капотом", обидва операнди приводяться до типу str, а потім з першого
# операнду видаляється перше входження значення другоо операнду, якщо такий
# має місце. Результатом віднімання стане новий об'єкт класу String. Якщо в
# першому операнді немає значення другого операнду, то результатом віднімання
# стане перший операнд без змін. Приклади виконання:
#
# String('New bala7nce') - 7               ->    'New balance'
# String('New balance') - 'bal'            ->    'New ance'
# String('New balance') - 'Bal'            ->    'New balance'
# String('pineapple apple pine') - 'apple' ->    'pine apple pine'
# String('New balance') - 'apple'          ->    'New balance'
# String('NoneType') - None                ->    'Type'
# String(55678345672) - 7                  ->    '5568345672'
#
# *Важливо! Результатом додавання або віднімання завжди буде об'єкт типу String.




# Рішення викладача:

class String(str):

    def __add__(self, other):
        return String(super().__add__(str(other)))

    def __sub__(self, other):
        return String(self.replace(str(other), "", 1))