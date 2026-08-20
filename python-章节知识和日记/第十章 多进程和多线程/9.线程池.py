"""
线程池 :  
    a) 减少 线程 创建 和 销毁

    b) 可复用线程 


"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from threading import current_thread


def execute_task(num):
    """
    如果 num 是素数、则 返回 num, 否则 返回 None
    """
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            break 
    else:
        print(f"当前线程是: {current_thread().name}、 素数是 {num}")
        return num 



if __name__ == "__main__":
    
    # 构建一个 线程池 执行者 、并设置 执行任务 需要的 线程数量
    executor = ThreadPoolExecutor(max_workers=10)

    # 使用 submit 方法 执行 指定的任务 、并 获取 任务执行的结果
    futures = [executor.submit(execute_task, num)  for num in range(2, 1000000)]

    # 如何 获取 未来对象 它的结果 、阻塞式等待 线程执行的结果
    for f in as_completed(futures):
        # 获取 f 对应的 计算结果 
        if f.result() is not None:
            print(f.result())

