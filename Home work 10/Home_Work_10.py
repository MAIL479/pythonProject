# Polymorphism
class Car:
    def wheels(self):
        print("4 wheels")

    def mode_of_transport(self):
        print("Private usage")


class Bus:
    def wheels(self):
        print("8 wheels")

    def mode_of_transport(self):
        print("Public usage")


car1 = Car()
bus1 = Bus()

vehicles = [car1, bus1]

for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
    print()


class Vehicle:
    def desc(self):
        pass

    def wheels(self):
        pass


class Bike(Vehicle):
    def desc(self):
        print("This is a bike")

    def wheels(self):
        print("2 wheels")


class Truck(Vehicle):
    def desc(self):
        print("This is a truck")

    def wheels(self):
        print("10 wheels")


bike = Bike()
truck = Truck()

vehicles = [bike, truck]

for vehicle in vehicles:
    vehicle.desc()
    vehicle.wheels()
    print()


# Encapsulation

class MyClass:
    def __init__(self):
        self._a = 10
        self.__a = 20


obj = MyClass()

# Доступ до змінної _a (protected)
print(obj._a)  # Виведе 10

# Доступ до змінної __a (private)
# Спроба доступу викличе помилку AttributeError
print(obj.__a)
# AttributeError: 'MyClass' object has no attribute '__a'