from threading import Thread 
import time

def cpu_bound():
    """cpu密集型任务 GIL 导致多线程无法加速"""
    total = 0 
    for i in range(10000000):
        total += i
    return total

#单线程
start = time.time()
cpu_bound()
cpu_bound()
print(f"单线程执行时间: {time.time() - start:.2f}s")

#多线程  ~ 不会变快 对于 CPU 密集型任务，多线程无法利用多核 CPU 加速。
start = time.time()
t1 = Thread(target=cpu_bound)
t2 = Thread(target=cpu_bound)
t1.start();t2.start()
t1.join();t2.join()
print(f"多线程执行时间: {time.time() - start:.2f}s")