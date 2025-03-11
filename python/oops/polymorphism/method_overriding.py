class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal):
    animal.speak()

animal = Animal()
dog = Dog()
cat = Cat()

make_animal_speak(animal)  # Output: Animal speaks
make_animal_speak(dog)  # Output: Dog barks
make_animal_speak(cat)  # Output: Cat meows