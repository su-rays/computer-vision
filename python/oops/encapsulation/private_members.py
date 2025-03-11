'''Encapsulation restricts the direct access to the data members and can only be modified through methods'''


class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

    def __private_method(self):
        return "This is a private method"

    def public_method(self):
        return self.__private_method()

# Creating an instance of MyClass
obj = MyClass()

# Accessing private attribute directly will raise an AttributeError
# print(obj.__private_attribute)  # This will raise an error

# Accessing private method directly will raise an AttributeError
# print(obj.__private_method())  # This will raise an error

# Accessing private members through a public method
print(obj.public_method())  # Output: This is a private method