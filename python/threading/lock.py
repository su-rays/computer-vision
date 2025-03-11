from threading import *

lock = RLock()

number = 100

def add_data(num):
    lock.acquire()
    global number
    print(f"number before addition: {number}")
    number += num
    print(f"number after addition: {number}")
    lock.release()

def sub_data(num):
    lock.acquire()
    global number
    print(f"number before subtraction: {number}")
    number -= num
    print(f"number after subtraction: {number}")
    lock.release()

def mul_data(num):
    lock.acquire()
    global number
    print(f"number before multiplying: {number}")
    number *= num
    print(f"number after multiplying: {number}")
    lock.release()

def div_data(num):
    lock.acquire()
    global number
    print(f"number before dividing: {number}")
    number /= num
    print(f"number after dividing: {number}")
    lock.release()

thread1 = Thread(target=add_data, args=(10,))
thread2 = Thread(target=sub_data, args=(20,))
thread3 = Thread(target=mul_data, args=(10,))
thread4 = Thread(target=div_data, args=(20,))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("all operations are accomplished")