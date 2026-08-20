"""
线程间的通信 :

    Condition 条件 

        wait() : 等待 、 如果一个线程调用 wait 方法, 会立即进入 等待状态、 让出 CPU 执行权限 和 锁

        notify() :  唤醒 。  随机唤醒 相同条件下   处于 等待的 1 个 线程 

        notify_all() : 唤醒所有。 唤醒 相同条件下 所有处于等待状态的 线程

    Condition 必须在 原子操作(锁块)中使用 


编写一个 生产者 、负责 摘苹果 、 当 苹果数量 超过 50个的时候,  停止 摘苹果 。 并通知 消费者 负责 吃苹果

编写一个 消费者、 负责 吃苹果 、 当 苹果 数量 等于 0 的时候，停止吃苹果、通知 生产者 负责摘苹果


队列 Queue :

    put(x) :  向队列中 添加数据 、 如果队列 已满、则 会阻塞式等待 
    put_nowait(x) 向队列中 添加数据, 如果队列已满、 直接抛出错误

    get() :  从 队列获取一条数据、 如果队列是 空的、 则会阻塞式等待 
    get_nowait() :   从 队列获取一条数据、 如果队列是 空的、 直接抛出错误

    qsize() : 获取 队列中 数据的个数 
    empty() : 判断 队列是否是 空的 
    full()  : 判断 队列是否是 满的 



"""
from threading import Thread, Condition
from queue import Queue
import time, random


class Apple:
    """苹果类"""
    __number = 0 

    def __init__(self):
        self.num = self.__class__.__number + 1 
        self.__class__.__number += 1

    def __repr__(self):

        return f"{self.__class__.__name__}({self.num})"


class Productor(Thread):

    def __init__(self, name, queue: Queue, pro_condition: Condition,  cus_condition: Condition, is_wait=False):
        super().__init__(name=name)
        self.queue = queue 
        self.pro_cond = pro_condition
        self.cus_cond = cus_condition
        self.is_wait = is_wait

    def run(self):
        # 负责 摘苹果 
        while True:
            # 对 生产者 进入 加锁处理 
            with self.pro_cond:
                if not self.queue.full():
                    # 创建一个 苹果对象 (摘苹果)
                    apple = Apple() 
                     # 存入到 队列中 
                    self.queue.put(apple)
                    # 输出 信息 
                    print(f"生产者 {self.name} 正在摘苹果、当前苹果数量 {self.queue.qsize()}")
                else:
                    # 将生产者 进入 等待状态
                    print(f"苹果数量 已满、生产者 {self.name} 停止摘苹果")
                    self.pro_cond.wait()
                    self.is_wait = True

            # 添加延迟时间
            time.sleep(random.uniform(0.5, 1))

            # 对消费者 加锁处理、负责 唤醒消费者
            with self.cus_cond:
                if self.queue.full():
                    print(f"正在唤醒所有的消费者")
                    # 唤醒所有的消费者
                    self.cus_cond.notify_all()



class Consumer(Thread):

    def __init__(self, name, queue: Queue, pro_condition: Condition,  cus_condition: Condition, is_wait=False):
        super().__init__(name=name)
        self.queue = queue 
        self.pro_cond = pro_condition
        self.cus_cond = cus_condition
        self.is_wait = is_wait

    def run(self):
        # 如果 苹果 不满、则 等待 
        with self.cus_cond:
            if not self.queue.full():
                self.is_wait = True
                self.cus_cond.wait()
            
        while True:
           
            with self.cus_cond:
                if not self.queue.empty():
                    # 负责 吃苹果 
                    apple = self.queue.get()
                    print(f"消费者 {self.name} 正在吃苹果、苹果编号是 {apple.num}")
                else:
                    # 停止 吃苹果
                    print(f"消费者 {self.name} 停止吃苹果")
                    self.is_wait = True
                    self.cus_cond.wait()

            time.sleep(random.uniform(2, 2.5))


def check_consumer_status(consumer_list, pro_cond, pro):

    while True:
        if all([con.is_wait for con in consumer_list]):
            # 唤醒 生产者 
            with pro_cond:
                if not pro.is_wait:
                    print("正在唤醒所有的生产者")
                    pro_cond.notify_all()
                    pro.is_wait = True


if __name__ == "__main__":
    
    pro_cond = Condition()
    cus_cond = Condition() 
    # 创建一个队列、并设置 队列的最大长度
    apple_queue = Queue(maxsize=50)

    # 创建 一个 生产者、负责 摘苹果 
    productor = Productor("机器人-0001", apple_queue, pro_cond, cus_cond)
    productor.start()


    consumer_list = []
    persons = ["小明", "小花", "小李"]
    for i in range(3):
        consumer = Consumer(persons[i], apple_queue, pro_cond, cus_cond)
        consumer_list.append(consumer)
        consumer.start()

    # 开启一个线程、 专门 检查消费者的 等待状态 
    thread = Thread(target=check_consumer_status, args=(consumer_list, pro_cond, productor))

    thread.start()

