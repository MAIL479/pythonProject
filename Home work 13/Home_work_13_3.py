try:
    # Арифметична операція
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero.")
except Exception as e:
    print("An error occurred:", e)

try:
    # Робота з колекціями
    my_list = [1, 2, 3]
    print(my_list[5])  # Спроба отримати елемент за індексом, якого немає у списку
except IndexError:
    print("Error: Index out of range.")
except Exception as e:
    print("An error occurred:", e)