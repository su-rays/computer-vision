import threading
import time


# Target function
def worker(id, delay, msg):
    """Function that will run in a separate thread."""
    time.sleep(delay)
    print(f"Thread-{id}: {msg}")

# Creating a thread using all possible arguments
t = threading.Thread(
    group=None,             # 'group' is always None (reserved for future use)
    target=worker,          # Target function
    name="CustomThread",    # Custom thread name
    args=(1, 2, "Hello from Thread!"),  # Positional arguments for target function
    kwargs={},              # Keyword arguments (empty in this case)
    daemon=True             # Runs as a daemon thread, it stops automatically when all threads stoped else keep running on background
)

print(dir(threading))
# Start the thread
t.start()

# Wait for the thread to finish
t.join()

# Check thread properties
print(f"Thread Name: {t.name}")
print(f"Is Daemon: {t.daemon}")
print(f"Is Alive: {t.is_alive()}")
