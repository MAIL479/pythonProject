# python file read/write. Context manager.

# Задача 1: Записати рядок у файл

# Використовуючи контекстний менеджер
with open("file.txt", "w") as file:
    file.write("Hello, world!")

# Задача 2: Прочитати вміст файлу та вивести на консоль

# Використовуючи класичний підхід
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()

# Задача 3: Додати ще один рядок до файлу

# Використовуючи контекстний менеджер
with open("file.txt", "a") as file:
    file.write("\nThis is another line.")

# Задача 4: Прочитати всі рядки з файлу та вивести на консоль

# Використовуючи класичний підхід
file = open("file.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

# Задача 5: Записати у файл все, що користувач введе з консолі

# Використовуючи контекстний менеджер
with open("file.txt", "a") as file:
    while True:
        user_input = input("Введіть рядок (або 'exit' для завершення): ")
        if user_input == "exit":
            break
        file.write(user_input + "\n")