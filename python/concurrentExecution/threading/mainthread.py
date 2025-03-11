import threading

main_thread = threading.main_thread()
print(f"Main Thread: {main_thread.name}")
