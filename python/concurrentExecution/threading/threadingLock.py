import threading 

lock = threading.lock()

counter = 0

def increment():
    global increment
    with lock:
        temp = counter
        temp += 1
        counter = temp

threads = [threading.Thread(target=increment) for _ in range(100)]

for t in threads:
    t.start()

for t in threads:
    t.join()

    