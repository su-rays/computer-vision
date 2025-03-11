import threading

def delay_func():
    print("delayed it")

thread = threading.Timer(interval=5, function=delay_func, args=(), kwargs={})

print(dir(threading))

thread.start()
thread.join(timeout=None)