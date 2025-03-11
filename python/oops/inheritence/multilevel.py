# Grandparent class
class Grandparent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} is speaking."

# Parent class inheriting from Grandparent
class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name} is {self.age} years old."

# Child class inheriting from Parent
class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def speak(self):
        return f"{self.name} is {self.age} years old and goes to {self.school}."

# Creating an object
child = Child("Bob", 10, "ABC School")
print(child.speak())  # Output: Bob is 10 years old and goes to ABC School.