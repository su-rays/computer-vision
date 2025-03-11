class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"

    def public_method(self):
        return "This is a public method"

# Creating an instance of MyClass
obj = MyClass()

# Accessing public attribute
print(obj.public_attribute)  # Output: I am public

# Accessing public method
print(obj.public_method())  # Output: This is a public method