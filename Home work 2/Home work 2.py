# Змінні
variable = "Hello"
Variable = "World"
_var = "Python"
var_two_words = "Two words"
var_number = 42
CONSTANT = "I am constant"
cReAtIvE_vArIaBlE = "I am creative"

# Виведення результатів арифметичних операцій
print(2 + 3)
print(5 - 2)
print(10 / 2)
print(4 * 5)
print(2 ** 3)
print(10 // 3)
print(10 % 3)
print((2 + 3) * 4)  # Поєднання операцій

# Оператори дії з присвоєнням
x = 5
x += 2
print(x)  # Виведе 7

y = 10
y -= 3
print(y)  # Виведе 7

# Інструкції if/else та оператори порівняння
a = 5
b = 10

if a < b:
    print("a < b")
else:
    print("a >= b")

if a != 0:
    result = b / a
    print(result)
else:
    print("a cannot be zero")

if a == b:
    print("a equals b")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")

if variable == Variable:
    print("Variables are equal")
else:
    print("Variables are not equal")

if variable != _var:
    print("Variables are not equal")
else:
    print("Variables are equal")

# Креативний варіант
if "creative" in cReAtIvE_vArIaBlE.lower():
    print("I am creative!")
else:
    print("I am not creative!")