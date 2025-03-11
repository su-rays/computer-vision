# Superclass 1
class A:
    def greet(self):
        return "Hello from A."

# Superclass 2
class B(A):
    def greet(self):
        return "Hello from B."

# Superclass 3
class C(A):
    def greet(self):
        return "Hello from C."

# Subclass inheriting from B and C
class D(B, C):
    def greet(self):
        return "Hello from D."

# Creating an object
d = D()
print(d.greet())  # Output: Hello from D.
print(D.mro())    # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]