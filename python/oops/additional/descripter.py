class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Person:
    age = Descriptor("age")

p = Person()
p.age = 25
print(p.age)  # Output: 25
