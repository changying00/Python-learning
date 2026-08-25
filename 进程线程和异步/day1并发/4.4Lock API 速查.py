import threading
lock = threading.Lock()   # 创建锁

lock.acquire()            # 获取锁（阻塞）
lock.acquire(timeout=5)   # 超时获取（返回 True/False）
lock.release()            # 释放锁

# 推荐使用 context manager
with lock:
    # 受保护的代码
    pass

# 尝试非阻塞获取
if lock.locked():
    print("锁已被占用")