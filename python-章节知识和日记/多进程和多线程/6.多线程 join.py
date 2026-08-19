from threading import Thread 
import time
"""
join() :  线程对象 有一个方法join,  它的作用 是 加入 当前线程 并阻塞 当前线程
使用 多线程 计算 1000,000 以内的所有素数
"""
import time 
from threading import Thread , Lock
def get_prime(range_seq, prime_list: list, lock):
    # 计算 range_seq 中所有的素数 
    for x in range_seq:
        for y in range(2, int(x ** 0.5) + 1):
            if x % y == 0:
                break 
        else:
            with lock:
                # print(x)
                prime_list.append(x)
if __name__ == "__main__":

    # 定义一个 列表、用来存储所有的素数 
    prime_list = []
    # 创建一个 互斥锁 
    lock = Lock() 

    # 创建一个 容器，存储所有的 线程 对象 
    thread_pools = []

    # 获取 起始时间 
    start = time.time()
    for i in range(20):
        # 创建 10 个线程对象 
        thread = Thread(target=get_prime, args=(range(i * 50000, (i+1) * 50000), prime_list, lock))
        # 启动 线程 
        thread.start()
        thread_pools.append(thread)
    for th in thread_pools:
        th.join()

    end = time.time() 
    print(f"共消耗时长 : {end - start:.2f}秒")
    # 当 10 个线程 结束了、就 获取到 了所有 素数 
    print(len(prime_list))




# start = time.time()
# for x in range(2, 1000001):
#     # 从 2 ~ x 的算术平方根 
#     for y in range(2, int(x ** 0.5) + 1):

#         if x % y == 0:
#             break 
#     # else:
#     #     print(x)

# end = time.time()

# print(f"共消耗时长 {end-start:.2f}s")