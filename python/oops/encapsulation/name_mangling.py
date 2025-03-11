class MyClass:
    def __init__(self):
        self.__private_attribute = "I am private"

# Creating an instance of MyClass
obj = MyClass()

# Accessing private attribute using name mangling
print(obj._MyClass__private_attribute)  # Output: I am private