'''A class is the blue print for creating objects, while object is the instance of the class'''

class Car:
    # Class attribute
    wheels = 4

    # Constructor
    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

    # Instance method
    def display_info(self):
        return f"{self.brand} {self.model} has {self.wheels} wheels."

    # Class method
    @classmethod
    def set_wheels(cls, new_wheels):
        cls.wheels = new_wheels

    # Static method
    @staticmethod
    def is_electric(fuel_type):
        return fuel_type == "electric"

# Create objects
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

# Access instance attributes and methods
print(car1.display_info())  # Output: Tesla Model S has 4 wheels.
print(car2.display_info())  # Output: Toyota Corolla has 4 wheels.

# Modify class attribute using class method
Car.set_wheels(6)
print(car1.display_info())  # Output: Tesla Model S has 6 wheels.

# Use static method
print(Car.is_electric("electric"))  # Output: True