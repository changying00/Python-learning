from threading import Thread
import time
#守护线程 主线程退出时自动终止
def daemon_worker():
    while True:
        print("守护线程正在运行...")
        time.sleep(0.85)

#非守护线程、主线程退出后，非守护线程仍然会继续运行
def normal_worker():
    for i in range(5):
        print(f"普通线程{i}")
        time.sleep(1)
#守护线程创建
t1 = Thread(target=daemon_worker, daemon=True)

#非守护线程创建
t2 = Thread(target = normal_worker)

t1.start()

t2.start()

# 主线程结束后：
# 普通线程仍然会继续运行
# 守护线程也会继续运行
# 只有当所有非守护线程都结束，
# Python进程准备退出时，守护线程才会随进程一起终止。
#join() 的作用是：
#让当前线程等待另一个线程执行完。
time.sleep(0.3)
print("主线程退出，非守护线程继续运行...")
#守护线程是否继续运行，看的不是“主线程死没死”，而是“整个 Python 进程是不是要退出”。
# 守护线程适合：后台监控、定时心跳。普通线程适合：需要确保完成的任务。
