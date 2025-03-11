import threading
import time
import random

def barrier_action():
    print("Barrier action executed by one thread before releasing all threads.")

def worker(barrier: threading.Barrier, thread_id: int):
    try:
        print(f"Thread-{thread_id} is performing some work.")
        time.sleep(random.uniform(0.5, 2))  # Simulating work
        print(f"Thread-{thread_id} is waiting at the barrier.")
        index = barrier.wait()  # Wait at the barrier
        print(f"Thread-{thread_id} passed the barrier with index {index}.")
    except threading.BrokenBarrierError:
        print(f"Thread-{thread_id} detected a broken barrier!")

def main():
    num_threads = 5
    barrier = threading.Barrier(parties=num_threads, action=barrier_action, timeout=5)
    
    threads = [threading.Thread(target=worker, args=(barrier, i)) for i in range(num_threads)]
    
    for t in threads:
        t.start()
    
    time.sleep(3)  # Simulate some condition to reset the barrier
    if random.choice([True, False]):
        print("Resetting the barrier due to some condition.")
        barrier.reset()
    
    for t in threads:
        t.join()
    
    print(f"Barrier broken status: {barrier.broken}")
    print(f"Threads currently waiting: {barrier.n_waiting}")
    print(f"Total parties required: {barrier.parties}")
    
    # Aborting the barrier
    print("Aborting the barrier...")
    barrier.abort()
    print(f"Barrier broken status after abort: {barrier.broken}")

if __name__ == "__main__":
    main()
