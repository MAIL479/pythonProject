# Створити клас  з абстрактним методом. Створити об'єкт даного класу.

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class MyClass(MyAbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method.")

# Створення об'єкту класу MyClass
obj = MyClass()
obj.abstract_method()

# Створити клас який успадкований від класу ABC або metaclass=ABCMeta і створити його об'єкт.

from abc import ABC, ABCMeta

class MyAbstractClass(ABC):
    pass

class MyClass(MyAbstractClass):
    def __init__(self):
        print("MyClass object created.")

# Створення об'єкту класу MyClass
obj = MyClass()


# Створити абстрактний клас з абстрактним методом. Створити новий клас успадкований від абстрактного класу і створіть об'єкт нового класу.

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class MySubclass(MyAbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method in MySubclass.")

# Створення об'єкту класу MySubclass
obj = MySubclass()
obj.abstract_method()