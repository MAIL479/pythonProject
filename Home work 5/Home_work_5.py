# 1. Tuple
# Створити кортеж, що містить ряд чисел
my_tuple = (1, 2, 3, 4, 5, 6, 7)
print("Tuple:", my_tuple)

# 2. Set
# Створити перший set
set_1 = {1, 2, 3, 4, 5, 6, 7}
print("Set 1:", set_1)

# Створити другий set
set_2 = {5, 6, 7, 8, 9, 10, 11}
print("Set 2:", set_2)

# Розширити перший set за допомогою команди .add(0)
set_1.add(0)
print("Set 1 після додавання 0:", set_1)

# Виконати команду .intersection() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
intersection_set = set_1.intersection(set_2)
print("Результат intersection():", intersection_set)

# Виконати команду .difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
difference_set = set_1.difference(set_2)
print("Результат difference():", difference_set)

# Виконати команду .symmetric_difference() на першому сеті передаючи в команду другий сет як аргумент, результат зберегти у нову змінну.
symmetric_difference_set = set_1.symmetric_difference(set_2)
print("Результат symmetric_difference():", symmetric_difference_set)
