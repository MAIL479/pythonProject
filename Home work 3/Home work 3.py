# Форматування рядків:

name = "John"
age = 25
formatted_string = "Мене звати {}. Мені {} років.".format(name, age)
print(formatted_string)

name = "Mary"
age = 30
formatted_string = f"Мене звати {name}. Мені {age} років."
print(formatted_string)

# Робота з методами рядка:

text = "Привіт, світе!"
split_text = text.split()
print(split_text)

uppercase_text = text.upper()
print(uppercase_text)

lowercase_text = text.lower()
print(lowercase_text)

capitalized_text = text.capitalize()
print(capitalized_text)

index = text.find("світе")
print(index)

# Робота зі списками:

list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
print(list2)

list1.append(6)
print(list1)

list1.insert(2, 10)
print(list1)

list3 = [7, 8, 9]
list1.extend(list3)
print(list1)

popped_element = list1.pop()
print(popped_element)

list1.remove(4)
print(list1)

value = list1[2]
print(value)

# Зрізи (slices):

string = "Hello, world!"
reversed_string = string[::-1]
print(reversed_string)

list4 = [1, 2, 3, 4, 5]
reversed_list = list4[::-1]
print(reversed_list)

slice_list = list4[1:7:2]
print(slice_list)

slice_string = string[2:8]
print(slice_string)


