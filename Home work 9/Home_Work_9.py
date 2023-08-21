# Lambda

# Лямбда функція, що друкує символ задану кількість разів


print_char = lambda char, count=100: print(char * count)

# Приклад використання

print_char('#', 5) # Виведе '#####'
print_char('', 10) # Виведе '*********'
print_char('A') # Виведе 'AAAAAAAAAA' (використовується значення за замовчуванням)

# Лямбда функція, що повертає більше з двох чисел

get_max = lambda x, y: x if x > y else y

# Приклад використання

result = get_max(5, 10)
print(result) # Виведе 10

# Лямбда функція, що завжди повертає 10

always_10 = lambda: 10

# Приклад використання

result = always_10()
print(result) # Виведе 10


# Decorators

def make_bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def make_italic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

def make_underline(fn):
    def wrapper():
        return "<u>" + fn() + "</u>"
    return wrapper

@make_bold
@make_italic
@make_underline
def say_hello():
    return "hello world"

result = say_hello()
print(result)  # Виведе "<b><i><u>hello world</u></i></b>"



# List comprehension

# Завдання 1
lst1 = [44, 54, 64, 74, 104]
lst2 = [x + 6 for x in lst1]
print(lst2)  # Виведе [50, 60, 70, 80, 110]

# Завдання 2
lst3 = [2, 4, 6, 8, 10, 12, 14]
list4 = [x ** 2 for x in lst3]
print(list4)  # Виведе [4, 16, 36, 64, 100, 144, 196]

# Завдання 3
car_dict = {
    "Sedan": 1500,
    "SUV": 2000,
    "Pickup": 2500,
    "Minivan": 1600,
    "Van": 2400,
    "Semi": 13600,
    "Bicycle": 7,
    "Motorcycle": 110
}
list5 = [key.upper() for key, value in car_dict.items() if value <= 5000]
print(list5)  # Виведе ['SEDAN', 'SUV', 'PICKUP', 'MINIVAN', 'VAN', 'BICYCLE', 'MOTORCYCLE']