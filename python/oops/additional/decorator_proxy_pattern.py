# Decorator Pattern
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello"

print(greet())  # Output: HELLO

# Proxy Pattern
class RealImage:
    def display(self):
        print("Displaying image.")

class ProxyImage:
    def __init__(self):
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage()
        self.real_image.display()

proxy = ProxyImage()
proxy.display()  # Output: Displaying image.
