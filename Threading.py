import threading
import time
import random

lock = threading.Lock()


def show_number(number):
    with lock:
        wait_time = random.uniform(0, 0.5)
        time.sleep(wait_time)
        print(str(number) + ", ")


for n in range(1, 11):
    threading.Thread(target=show_number,
                     args=[n]
                     ).start()

# result without lock: 8, 4, 9, 6, 1, 10, 7, 3, 2, 5
# result with lock: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
