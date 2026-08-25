import threading
import time
counter = 0

def increment():
    global counter
    for _ in range(1000):
        time.sleep(0.01)  # 故意让线程切换
        counter += 1  # 这不是原子操作！

# 两个线程同时 increment
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()

print(f"期望: 2000, 实际: {counter}")

    