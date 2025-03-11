
# Factory Method Pattern
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    animals = {"dog": Dog, "cat": Cat}
    return animals.get(animal_type, Dog)()

animal = animal_factory("cat")
print(animal.speak())  # Output: Meow!


# Abstract Factory Pattern
from abc import ABC, abstractmethod

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

factory = DogFactory()
dog = factory.create_animal()
print(dog.speak())  # Output: Woof!
