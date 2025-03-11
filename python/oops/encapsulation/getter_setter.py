class MyClass:
    def __init__(self):
        self.__private_attribute = None

    def get_private_attribute(self):
        return self.__private_attribute

    def set_private_attribute(self, value):
        if isinstance(value, str):
            self.__private_attribute = value
        else:
            raise ValueError("Value must be a string")

# Creating an instance of MyClass
obj = MyClass()

# Setting private attribute using setter method
obj.set_private_attribute("Hello")

# Getting private attribute using getter method
print(obj.get_private_attribute())  # Output: Hello

# Trying to set an invalid value
# obj.set_private_attribute(123)  # This will raise a ValueError