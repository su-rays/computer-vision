import threading
import time

sem = threading.BoundedSemaphore(2)  # Max 2 threads allowed

def task(name):
    sem.acquire()
    print(f"{name} acquired semaphore")
    time.sleep(2)
    sem.release()
    print(f"{name} released semaphore")

threads = [threading.Thread(target=task, args=(f"Thread-{i}",)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
