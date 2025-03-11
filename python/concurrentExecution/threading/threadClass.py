import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread Running: {i}")
    
t = MyThread()
t.start()
t.join()