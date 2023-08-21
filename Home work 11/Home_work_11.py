# Abstract class

from abc import ABC, abstractmethod

# Створення абстрактного класу з абстрактним методом
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Створення класу, успадкованого від абстрактного класу
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method in ConcreteClass")

# Створення об'єкту класу ConcreteClass
obj_concrete = ConcreteClass()
obj_concrete.abstract_method()