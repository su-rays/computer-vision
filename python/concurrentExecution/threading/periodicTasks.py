import threading
import time

def periodic_task():
    while True:
        print("Running periodic task")
        time.sleep(2)

t = threading.Thread(target=periodic_task, daemon=True)
t.start()

time.sleep(7)  # Main thread runs for a while
print("Main thread exiting...")
