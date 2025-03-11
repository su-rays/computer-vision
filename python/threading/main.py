import threading
import multiprocessing

# print(dir(threading))
print(dir(multiprocessing))

# available_seats = 2

# def reserve(seat_needed):
#     global available_seats
#     print(f"available seats are: {available_seats}")
#     if available_seats >= seat_needed:
#         print(f" {seat_needed} seat is allocated to {threading.current_thread().name}")
#         available_seats -= 1
#     else:
#         print("sorry all seat are reserved!")
        

# thread1 = threading.Thread(group=None, target=reserve, name="raj", args=(1,), kwargs={})
# thread2 = threading.Thread(group=None, target=reserve, name="seetal", args=(1,), kwargs={})

# thread1.start()
# thread2.start()