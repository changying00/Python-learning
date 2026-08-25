from threading import Thread,Lock
import time
counter = 0
lock = Lock()

def safe_increment():
    global counter
    for _ in range(1000):
        time.sleep(0.01)  # 故意让线程切换
        with lock:  # 使用锁来保护临界区
            counter += 1  # 这不是原子操作！        

t1 = Thread(target=safe_increment)
t2 = Thread(target=safe_increment)
t1.start(); t2.start()
t1.join(); t2.join()
print(f"期望: 2000, 实际: {counter}")