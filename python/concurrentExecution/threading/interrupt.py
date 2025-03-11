import threading
import time

stop_event = threading.Event()

def long_task():
    while not stop_event.is_set():
        print("Working...")
        time.sleep(1)

t = threading.Thread(target=long_task)
t.start()

time.sleep(3)
stop_event.set()
t.join()
print("Thread stopped.")
