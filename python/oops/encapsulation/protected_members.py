class MyClass:
    def __init__(self):
        self._protected_attribute = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

# Creating an instance of MyClass
obj = MyClass()

# Accessing protected attribute directly (not recommended)
print(obj._protected_attribute)  # Output: I am protected

# Accessing protected method directly (not recommended)
print(obj._protected_method())  # Output: This is a protected method