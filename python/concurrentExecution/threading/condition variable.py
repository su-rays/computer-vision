import threading

condition = threading.Condition()
ready = False

def consumer():
    global ready
    with condition:
        condition.wait_for(lambda: ready)
        print("Consumer received data!")

def producer():
    global ready
    with condition:
        ready = True
        condition.notify_all()

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()
t1.join()
t2.join()
