# Рядки
# Навести приклад простого рядка
simple_string = "Hello, world!"

# Навести приклад багаторядкового рядка (Вірш, хоку - щоб показати форматування)
multiline_string = """In the cherry blossom's shade
there's no such thing
as a stranger"""

# Навести приклад рядка з ігноруванням екрануючих символів (Raw)
raw_string = r"C:\Users\Username\Documents"

# Навести приклад форматування довгих рядків
long_string = (
    "This is a long string that needs to be formatted. "
    "It spans multiple lines for better readability."
)

print("Рядки:")
print("Простий рядок:", simple_string)
print("Багаторядковий рядок:")
print(multiline_string)
print("Рядок з ігноруванням екрануючих символів:", raw_string)
print("Форматування довгих рядків:", long_string)
print()


# Списки
# Створити простий список
simple_list = [1, 2, 3, 4, 5]

# Створити змінну з посиланням на перший список
reference_list = simple_list

# Створити поверхову (Shallow copy) копію першого списка
shallow_copy_list = simple_list.copy()

# Створити глибоку (повну) (Deep copy) першого списка
import copy
deep_copy_list = copy.deepcopy(simple_list)

print("Списки:")
print("Простий список:", simple_list)
print("Змінна з посиланням на перший список:", reference_list)
print("Поверхова копія першого списку:", shallow_copy_list)
print("Глибока копія першого списку:", deep_copy_list)
print()

# Змінити перший список і ще раз вивести значення всіх списків
simple_list[0] = 10

print("Змінений перший список:", simple_list)
print("Змінена змінна з посиланням на перший список:", reference_list)
print("Змінена поверхова копія першого списку:", shallow_copy_list)
print("Змінена глибока копія першого списку:", deep_copy_list)
print()

# Словники
# Створити пустий словник одним з наведених в лекції способів
empty_dict = {}
# Або
empty_dict = dict()

# Створити новий словник з 2-3 парами ключ:значення
new_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# Додати одну пару ключ:значення до першого словника
empty_dict['key'] = 'value'

# Додати до першого словника другий словник використовуючи .update()
empty_dict.update(new_dict)

# Видалити один елемент словника за допомогою .pop()
removed_value = empty_dict.pop('apple')

# Видалити один елемент за допомогою .popitem()
removed_item = empty_dict.popitem()

# Зробити глибоку копію першого словника в нову змінну
copied_dict = copy.deepcopy(empty_dict)

# Додати до нового словника новий ключ, а як значення передати перший словник
copied_dict['new_key'] = empty_dict

# Вивести список ключів
print("Словники:")
print("Пустий словник:", empty_dict)
print("Новий словник:", new_dict)
print("Словник після додавання пари ключ:значення:", empty_dict)
print("Словник після об'єднання з іншим словником:", empty_dict)
print("Видалений елемент:", removed_value)
print("Видалена пара ключ:значення:", removed_item)
print("Глибока копія першого словника:", copied_dict)
print("Список ключів:", list(copied_dict.keys()))
print()

# Вивести список значень
print("Список значень:", list(copied_dict.values()))
print()

# Тернарний if - 2 приклади
# Приклад 1:
x = 10
y = 20
max_value = x if x > y else y
print("Тернарний if (Приклад 1):", max_value)

# Приклад 2:
is_even = lambda n: "Even" if n % 2 == 0 else "Odd"
result = is_even(7)
print("Тернарний if (Приклад 2):", result)
print()

# Вкладені структури
# Створити 3 вимірний список (список 3х списків)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Змінити, будь який, елемент, будь якого, спику.
nested_list[1][2] = 99

print("Вкладені структури:")
print("3-вимірний список до зміни:", nested_list)
print("3-вимірний список після зміни:", nested_list)
print()

# Створити список зі вкладеним словником
nested_dict_list = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]

# Створити словник зі вкладеним списком
nested_list_dict = {'students': ['John', 'Jane', 'Alex'], 'count': 3}

# Зберегти вкладений список зі словника у нову змінну
nested_list_copy = copy.deepcopy(nested_list_dict['students'])

print("Список зі вкладеним словником:", nested_dict_list)
print("Словник зі вкладеним списком:", nested_list_dict)
print("Глибока копія вкладеного списку:", nested_list_copy)
print()

# Побітові операції
# Побітове AND:
# Порівняти два різних цілих і два однакових числа і вивести результат
a = 5  # 0101
b = 3  # 0011
result_1 = a & b
result_2 = a & a
print("Побітове AND:")
print("Результат (5 & 3):", result_1)  # 0001 (1)
print("Результат (5 & 5):", result_2)  # 0101 (5)

# Порівняти два різних рядка і два однакових рядка і вивести результат
str_1 = "Hello"
str_2 = "World"
result_3 = str_1 & str_2
result_4 = str_1 & str_1
print("Побітове AND (рядки):")
print("Результат ('Hello' & 'World'):", result_3)  # TypeError
print("Результат ('Hello' & 'Hello'):", result_4)  # TypeError
print()

# Повторити дії із пункту a для решти операцій (OR, XOR, NOT)
# Побітове OR:
result_5 = a | b
result_6 = a | a
print("Побітове OR:")
print("Результат (5 | 3):", result_5)  # 0111 (7)
print("Результат (5 | 5):", result_6)  # 0101 (5)

# Побітове XOR:
result_7 = a ^ b
result_8 = a ^ a
print("Побітове XOR:")
print("Результат (5 ^ 3):", result_7)  # 0110 (6)
print("Результат (5 ^ 5):", result_8)  # 0000 (0)

# Побітове NOT:
result_9 = ~a
result_10 = ~b
print("Побітове NOT:")
print("Результат (~5):", result_9)  # -6
print("Результат (~3):", result_10)  # -4
print()

# Виконати побітовий зсув вліво для:
# Цілого числа на 1, 2 та 3 біти
shifted_left_1 = a << 1
shifted_left_2 = a << 2
shifted_left_3 = a << 3
print("Побітовий зсув вліво:")
print("Результат (5 << 1):", shifted_left_1)  # 1010 (10)
print("Результат (5 << 2):", shifted_left_2)  # 10100 (20)
print("Результат (5 << 3):", shifted_left_3)  # 101000 (40)

# Рядка на 1, 2 та 3 біти
str_shifted_left_1 = str_1 << 1
str_shifted_left_2 = str_1 << 2
str_shifted_left_3 = str_1 << 3
print("Побітовий зсув вліво (рядок):")
print("Результат ('Hello' << 1):", str_shifted_left_1)  # TypeError
print("Результат ('Hello' << 2):", str_shifted_left_2)  # TypeError
print("Результат ('Hello' << 3):", str_shifted_left_3)  # TypeError
print()

# Виконати побітовий зсув вправо для:
# Цілого числа на 1, 2 та 3 біти
shifted_right_1 = a >> 1
shifted_right_2 = a >> 2
shifted_right_3 = a >> 3
print("Побітовий зсув вправо:")
print("Результат (5 >> 1):", shifted_right_1)  # 0010 (2)
print("Результат (5 >> 2):", shifted_right_2)  # 0001 (1)
print("Результат (5 >> 3):", shifted_right_3)  # 0000 (0)

# Рядка на 1, 2 та 3 біти
str_shifted_right_1 = str_1 >> 1
str_shifted_right_2 = str_1 >> 2
str_shifted_right_3 = str_1 >> 3
print("Побітовий зсув вправо (рядок):")
print("Результат ('Hello' >> 1):", str_shifted_right_1)  # TypeError
print("Результат ('Hello' >> 2):", str_shifted_right_2)  # TypeError
print("Результат ('Hello' >> 3):", str_shifted_right_3)  # TypeError
