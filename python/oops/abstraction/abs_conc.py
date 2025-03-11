from abc import ABC, abstractmethod

# Abstract class with both abstract and concrete methods
class Vehicle(ABC):
    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def start(self):
        pass

    # Concrete method (has an implementation)
    def stop(self):
        print("Vehicle stopped.")

# Concrete subclass
class Car(Vehicle):
    def start(self):
        print("Car started.")

# Concrete subclass
class Bike(Vehicle):
    def start(self):
        print("Bike started.")

# Usage
car = Car()
bike = Bike()

car.start()  # Output: Car started.
car.stop()   # Output: Vehicle stopped.

bike.start()  # Output: Bike started.
bike.stop()   # Output: Vehicle stopped.

# vehicle = Vehicle()  # This will raise an error because Vehicle is abstract