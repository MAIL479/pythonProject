# 1. Функція для виведення ряду Фібоначчі за допомогою рекурсії:

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Приклад використання
n = 10
fib_sequence = fibonacci_recursive(n)
print(fib_sequence)

# Виведе: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 2. Функція для підсумовування чисел у заданому діапазоні:

def sum_range(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

# Приклад використання
start = 5
end = 10
result = sum_range(start, end)
print(result)

# Виведе: 45

# 3. Функція для визначення пори року за номером місяця:

def season(month):
    if month in [1, 2, 12]:
        return "зима"
    elif month in [3, 4, 5]:
        return "весна"
    elif month in [6, 7, 8]:
        return "літо"
    elif month in [9, 10, 11]:
        return "осінь"
    else:
        return "Невірний номер місяця"

# Приклад використання
month = 7
result = season(month)
print(result)

# Виведе: літо

# 4. Функція для фільтрації списку та виведення елементів, що менші за певне значення:

def get_filtered(a):
    filtered_list = [num for num in a if num < 5]
    for num in filtered_list:
        print(num)

# Приклад використання
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
get_filtered(a)

# Виведе:
# 1
# 1
# 2
# 3

# 5. Приклад використання циклу for та умовного оператора if:

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Виведе:
# 2
# 4
# 6
# 8
# 10