what is threading?
    threading in python allows to run the tasks concurrently, and is used for the IO-bound tasks but is limited by GIL for CPU-bound tasks.

what is GIL?
    The Global Interpreter Lock (GIL) is a mutex that allows only one thread to execute Python bytecode at a time, even in multi-threaded programs. This makes Python threads ineffective for CPU-bound tasks but useful for I/O-bound tasks.


threading methods:
    Barrier:
    Boundedsemaphore:
    BrokenBarrierError:
    Condition:
    Event:
    ExceptHookArgs:
    Lock:
    RLock:
    Semaphore:
    T