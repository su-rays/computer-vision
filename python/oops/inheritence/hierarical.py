# Superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Subclass 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Subclass 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

# Subclass 3
class Cow(Animal):
    def speak(self):
        return f"{self.name} moos."

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Daisy")

print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.
print(cow.speak())  # Output: Daisy moos.