import threading
import time

def task():
    time.sleep(2)
    print("Task completed")

t = threading.Thread(target=task)
t.start()
print("Is thread alive?", t.is_alive())  # True
t.join()
print("Is thread alive?", t.is_alive())  # False
