import threading
import time

def task():
    time.sleep(2)

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

print(f"Active Threads: {threading.enumerate()}")

t1.join()
t2.join()
