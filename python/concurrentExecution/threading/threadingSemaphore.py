import threading
import time

sem = threading.Semaphore(2)  # Limit to 2 threads

def task(id):
    with sem:
        print(f"Thread {id} started")
        time.sleep(1)
        print(f"Thread {id} finished")

threads = [threading.Thread(target=task, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
