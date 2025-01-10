import threading
import time

def worker():
    print("Thread in execution")
    time.sleep(3)
    print("Thread finaly")

thread_one = threading.Thread(target=worker)

thread_one.start()

thread_one.join()

print("proces main finaly")