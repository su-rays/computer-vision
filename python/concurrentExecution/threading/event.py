import threading
import time

event = threading.Event()

def wait_for_event():
    print("Thread waiting for event...")
    event.wait()
    print("Event set, thread running!")

t = threading.Thread(target=wait_for_event)
t.start()

time.sleep(2)
print("Main thread setting event.")
event.set()

t.join()
