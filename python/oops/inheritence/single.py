# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Subclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating an object
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks.