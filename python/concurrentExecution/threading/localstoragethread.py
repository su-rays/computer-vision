import threading

thread_data = threading.local()

def process():
    thread_data.value = threading.current_thread().name
    print(f"Thread {thread_data.value} has its own data.")

t1 = threading.Thread(target=process, name="Thread-1")
t2 = threading.Thread(target=process, name="Thread-2")

t1.start()
t2.start()
t1.join()
t2.join()
