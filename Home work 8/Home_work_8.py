class PlaceHolder:
    pass


class MyClass:
    class_variable = "This is a class variable"

    def __init__(self, parameter):
        self.parameter = parameter

    def print_parameter(self):
        print(self.parameter)

    @staticmethod
    def static_method():
        print("This is a static method")


class DerivedClass(MyClass):
    def __init__(self, parameter1, parameter2):
        super().__init__(parameter1)
        self.parameter2 = parameter2

    def print_parameter2(self):
        print(self.parameter2)


# Приклад використання класів

# Клас PlaceHolder не має жодних методів або змінних

# Створюємо об'єкт класу MyClass і використовуємо його методи та змінні
my_obj = MyClass("Hello")
my_obj.print_parameter()  # Виведе: Hello
print(my_obj.class_variable)  # Виведе: This is a class variable
my_obj.static_method()  # Виведе: This is a static method

# Створюємо об'єкт класу DerivedClass і використовуємо його методи та змінні
derived_obj = DerivedClass("World", "Goodbye")
derived_obj.print_parameter()  # Виведе: World
print(derived_obj.class_variable)  # Виведе: This is a class variable
derived_obj.static_method()  # Виведе: This is a static method
derived_obj.print_parameter2()  # Виведе: Goodbye