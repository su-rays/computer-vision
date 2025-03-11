class MyClass:
    def __init__(self):
        self.__private_attribute = None

    @property
    def private_attribute(self):
        return self.__private_attribute

    @private_attribute.setter
    def private_attribute(self, value):
        if isinstance(value, str):
            self.__private_attribute = value
        else:
            raise ValueError("Value must be a string")

# Creating an instance of MyClass
obj = MyClass()

# Setting private attribute using property
obj.private_attribute = "Hello"

# Getting private attribute using property
print(obj.private_attribute)  # Output: Hello

# Trying to set an invalid value
# obj.private_attribute = 123  # This will raise a ValueError