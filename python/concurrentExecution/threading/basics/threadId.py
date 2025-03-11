import threading

def task():
    print(f"Thread ID: {threading.get_ident()}")

t = threading.Thread(group=None, target=task, name=None, args=(), kwargs={})
t.start()
t.join()
