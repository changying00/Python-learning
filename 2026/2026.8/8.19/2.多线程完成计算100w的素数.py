"""【多线程】使用多线程计算 一百万 以内的所有素数 (要求使用生成器表示一百万的数据)"""
import time
from threading import Thread , Lock
def get_prime(num, prime_list: list,  num_lock, list_lock):
    """计算这一批数字中的所有素数"""
    while True:
        # 多个线程竞争获取下一个数字
        with num_lock:
            try:
                yield_num = next(num)
            except StopIteration:
                return
        # 拿到数字之后，锁马上释放
        # 所以其他线程可以继续拿数字
        for x in range(2, int(yield_num ** 0.5) + 1):
            if yield_num % x == 0:
                break
        else:
            with list_lock:
                prime_list.append(yield_num)


if __name__ == "__main__":
    prime_list = []
    # 生成器
    num = (x for x in range(2, 1000000))
    # 生成器的锁
    num_lock = Lock()
    # 素数列表的锁
    list_lock = Lock()
    thread_pools = []

    start = time.time()
    for i in range(100):
        thread = Thread(
            target=get_prime,
            args=(num, prime_list, num_lock, list_lock)
        )

        thread.start()
        thread_pools.append(thread)

    for th in thread_pools:
        th.join()

    end = time.time()

    print(f"共消耗时长：{end - start:.2f}秒")
    print(f"素数数量：{len(prime_list)}")