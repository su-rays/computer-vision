''''Abstraction hides implementation details and only exposes necessary functionalities using ABC'''

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # No implementation, just a blueprint

# Concrete class
class Dog(Animal):
    def sound(self):
        return "Woof!"

# Concrete class
class Cat(Animal):
    def sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Woof!
print(cat.sound())  # Output: Meow!

# animal = Animal()  # This will raise an error because Animal is abstract