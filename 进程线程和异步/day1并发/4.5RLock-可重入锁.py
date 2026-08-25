from threading import Thread, RLock,Lock

rlock = RLock()  # 创建可重入锁对象
lock = Lock()    # 创建普通锁对象
def recursive_task(n):
    with rlock:
        if n > 0:
            print(f"递归层级: {n}")
            recursive_task(n - 1)  # 同一线程再次获取锁

recursive_task(3)
# 如果用 Lock，这里会死锁！
#普通 Lock 在同一线程中不能重复获取，否则会死锁。RLock 允许同一线程多次获取：