"""
进程实现方式 :

    1. 面向过程 

    Process(group=None, target=None, name=None, args=(), kwargs=None, daemon=False)


    2. 面向对象

    继承 Process 并重写 run 方法

怎么 启动进程 
    start()

进程间 数据 相互独立 、 进程间 如果 想要实现 数据共享，可以使用 队列存储 

"""
from multiprocessing import Process, current_process, Queue, Lock
import time, random 


def execute_task(queue, lock):

    while queue.qsize() > 0:
        # 模拟延迟 
        time.sleep(random.uniform(0.5, 1))
        with lock:
            if queue.qsize() > 0:
                # 获取 第一章票 
                ticket = queue.get()
                # 输出 票号 
                print(f"{current_process().name} 正在售票、票号是 {ticket} 、剩余 {queue.qsize()} 张")
    else:
        print(f"{current_process().name} 票已售罄")


if __name__ == "__main__":
    
    # 定义一个队列 
    queue = Queue(maxsize=100)
    # 开启 多个进程 进行售票 
    for x in range(1, 101):
        queue.put(x)

    lock = Lock()

    # 开启 两个进程 进行售票
    for _ in range(2):
        process = Process(target=execute_task, args=(queue, lock))
        # 启动 进程
        process.start()
