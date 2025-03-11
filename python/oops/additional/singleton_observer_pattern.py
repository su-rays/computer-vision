# singleton pattern
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True

# observer pattern
class Observer:
    def update(self, message):
        print(f"Received: {message}")

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify("Hello, Observer!")  # Output: Received: Hello, Observer!
