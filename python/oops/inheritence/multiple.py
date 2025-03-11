# Superclass 1
class Father:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello."

# Superclass 2
class Mother:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hi."

# Subclass inheriting from both Father and Mother
class Child(Father, Mother):
    def __init__(self, name):
        super().__init__(name)  # Calls the first superclass (Father)

    def speak(self):
        return f"{self.name} says both hello and hi."

# Creating an object
child = Child("Alice")
print(child.speak())  # Output: Alice says both hello and hi.

print(Child.mro()) # method resolution order
# Output: [<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]