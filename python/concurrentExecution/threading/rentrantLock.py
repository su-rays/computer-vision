import threading

lock = threading.RLock()

def task():
    with lock:
        print("Lock acquired once.")
        with lock:
            print("Lock acquired again!")

t = threading.Thread(target=task)
t.start()
t.join()
