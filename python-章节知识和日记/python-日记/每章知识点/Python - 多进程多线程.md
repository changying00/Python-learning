# 多进程 VS 多线程

## 名词解释

- 程序 ：是由一组指令组成的源代码 、是静态的
- 进程 ：是程序运行的产物、是动态的 、会随程序的运行而产生、程序的结束而死亡。
  > 一个程序 在运行期间 至少会产生 1个进程 ，这个进程被称为 主进程，
  > 
  > 主进程 可以 构建 多个 子进程、 形成 多进程 。
  > 
  > 进程 是 CPU 进行 ”任务分配" 的 最小单位, 善于处理 计算密集型任务
  > 
  > 多进程 之间 数据 相互独立
- 线程 :  是轻量级的进程 , 是 进程中 用来执行任务 的 工作单位
  > 一个 进程 至少 会产生 1个 线程 、这个线程 被称为 主线程
  > 
  > 主线程 可以 构建 多个 子线程 、形成 多线程 。
  > 
  > 是 CPU 进行 ”任务调度” 的最小单位 、善于处理 IO 密集型任务
  > 
  > 多线程 之间 共享 同一个进程中的 数据
- 并行 :   多个任务同时执行,   通常需要 多核 CPU 
- 串行 ： 多个任务 按照 顺序执行
- 并发 ： 多个任务 交替执行， 在同一个时刻 共同 争抢 一个资源。

# 多进程

## 多进程的实现方式 

- 使用 os.fork 实现 多进程 （只能应用在 Linux 操作系统中）
  ```python
  
  import time
  import os
  
  
  if __name__ == "__main__":
      # 创建一个 子进程
      # os.fork() 会 返回 2次结果 ， 如果返回一个 非 0 的数字， 代表 当前程序在 主进程中执行
      # 如果 返回 一个 0 ， 则 代表 当前程序 在 子进程中 执行
      print("我是主进程的代码...")
  
      # 定义一个列表
      ls = [1, 2, 3, 4, [5, 6]]
      # 开启一个 子进程
      pid = os.fork()
  
      if pid == 0:
          # 子进程的代码
          ls[0] = 100
          ls[-1][0] = 500
          print(f"子进程任务完成, ID是 {os.getpid()}, 主进程ID = {os.getppid()}",  ls)
  
      else:
          time.sleep(3)
          # 我是主进程中的代码
          print(f"子进程创建完成、且对应的进程ID = {pid}, 主进程的ID = {os.getpid()}", ls)
  
  ```
- 使用 Process 类创建 子进程 
  ```python
  from multiprocessing import Process
  import time
  
  
  def process_child_code():
      print("我是子进程中的代码")
  
  
  
  if __name__ == '__main__':
      # 使用 Process 类 创建一个 进程对象
      process = Process(target=process_child_code)
  
      # 如果希望 子进程 可以工作， 则 必须 启动子进程
      process.start()
      
      # 主进程 睡眠 0.2s ,  让出 cpu 的执行权限
      time.sleep(0.2)
  
      print("我是主进程中的代码....")
  
  ```
- 继承 Process 类 、并重写 类中的 run 方法 
  ```python
  from multiprocessing import Process
  import time
  
  
  class MyProcess(Process):
    
      def __init__(self, name):
          super().__init__(name=name)
  
      def run(self):
          """进程要执行的任务"""
          print("我是一个子进程代码")
  
  
  if __name__ == '__main__':
  
      # 创建一个 进程对象
      process = MyProcess()
  
      # 启动 进程
      process.start()
  
      time.sleep(0.2)
  
      print("主进程任务结束")
  ```

## 单机版售票系统

```python
from typing import List
import time
import random


class Ticket:
    """票"""

    def __init__(self, ticket_no):
        # 票
        self.ticket_no = ticket_no

    def __str__(self):
        return f"{self.__class__.__name__}({self.ticket_no})"


class TicketWindow:
    """售票窗口"""

    def __init__(self, name, ticket_list: List[Ticket]):
        self.name = name
        self.ticket_list = ticket_list

    def sell_ticket(self):
        while len(self.ticket_list) > 0:
            # 从 ticket_list 中 获取一张票
            ticket = self.ticket_list[0]
            # 将这张票 从列表中 移除
            self.ticket_list.pop(0)
            # 显示票号信息
            print(f"窗口是{self.name},票号是{ticket}, 剩余 {len(self.ticket_list)} 张票")
            # 每售票 1张票 、延迟 0.5 ~ 2 秒
            time.sleep(random.random() * 1.5 + 0.5)
        else:
            print("票已售罄")


if __name__ == '__main__':
    # 创建一个窗口窗口， 并初始化 100张票
    ticket_list = [Ticket(x) for x in range(1, 101)]

    ticket_window = TicketWindow("窗口1", ticket_list)

    # 进行售票
    ticket_window.sell_ticket()
```

## 多进程实现 售票系统 (面向过程版本)

```python
import time
import random
from multiprocessing import Process, current_process


class Ticket:
    """票"""

    def __init__(self, ticket_no):
        # 票
        self.ticket_no = ticket_no

    def __str__(self):
        return f"{self.__class__.__name__}({self.ticket_no})"


def sell_ticket(ticket_list):
    while len(ticket_list) > 0:
        # 从 ticket_list 中 获取一张票
        ticket = ticket_list[0]
        # 将这张票 从列表中 移除
        ticket_list.pop(0)
        # 显示票号信息
        print(f"窗口是{current_process().name},票号是{ticket}, 剩余 {len(ticket_list)} 张票")
        # 每售票 1张票 、延迟 0.5 ~ 2 秒
        time.sleep(random.random() * 1.5 + 0.5)
    else:
        print("票已售罄")


if __name__ == '__main__':
    # 创建一个窗口窗口， 并初始化 100张票
    ticket_list = [Ticket(x) for x in range(1, 101)]

    Process(target=sell_ticket, name="窗口1", args=(ticket_list[:25],)).start()
    Process(target=sell_ticket, name="窗口2", args=(ticket_list[25:50],)).start()
    Process(target=sell_ticket, name="窗口3", args=(ticket_list[50:75],)).start()
    Process(target=sell_ticket, name="窗口4", args=(ticket_list[75:],)).start()
```

## 多进程实现售票系统 （面向对象版本）

```python
from typing import List
import time
import random
from multiprocessing import Process


class Ticket:
    """票"""

    def __init__(self, ticket_no):
        # 票
        self.ticket_no = ticket_no

    def __str__(self):
        return f"{self.__class__.__name__}({self.ticket_no})"


class TicketWindow(Process):
    """售票窗口"""
    def __init__(self, name, ticket_list: List[Ticket]):
        super().__init__(name=name)
        self.ticket_list = ticket_list

    def sell_ticket(self):
        while len(self.ticket_list) > 0:
            # 从 ticket_list 中 获取一张票
            ticket = self.ticket_list[0]
            # 将这张票 从列表中 移除
            self.ticket_list.pop(0)
            # 显示票号信息
            print(f"窗口是{self.name},票号是{ticket}, 剩余 {len(self.ticket_list)} 张票")
            # 每售票 1张票 、延迟 0.5 ~ 2 秒
            time.sleep(random.random() * 1.5 + 0.5)
        else:
            print("票已售罄")

    def run(self):
        self.sell_ticket()


if __name__ == '__main__':
    # 创建一个窗口窗口， 并初始化 100张票
    ticket_list = [Ticket(x) for x in range(1, 101)]

    ticket_window = TicketWindow("窗口-1", ticket_list[:25]).start()
    ticket_window2 = TicketWindow("窗口-2", ticket_list[25:50]).start()
    ticket_window3 = TicketWindow("窗口-3", ticket_list[50:75]).start()
    ticket_window4 = TicketWindow("窗口-4", ticket_list[75:]).start()

```

## 进程通信技术 (IPC 机制)

> 进程间的数据是相互独立不共享的， 如果要实现 在多个进程间 进行 数据的交互 和通信， 就必须使用 IPC 通信机制 

### IPC 的实现方式 

- 管道 Pipe 技术 
- 共享 内存 Share Memory
- 队列 Queue 
- 信号量

###  Queue 

> 是一种数据结构、 特点是 FIFO 
> 
> queue = Queue()  :  创建一个 无限容器的 队列容器 
> 
> queue = Queue(maxsize=100)  :  创建一个 最大长度为 100 的 队列容器

- queue.put(obj)  :   向队列中添加数据、如果队列已满、则产生阻塞效果 
- queue.put_nowait(obj)  : 向队列中添加数据、如果队列已满、 则产生异常 
- queue.get()  :  获取队列中的 一条数据 、 如果队列 是 空的， 则 产生阻塞效果 
- queue.get_nowait() :  获取队列中的 一条数据 、 如果队列 是 空的，则产生异常
- queue.qsize()  :  获取队列中存储的数据个数 
- queue.empty()  :  获取队列是否是 空的 
- queue.full()  :  获取 队列是否是 满的

## 基于 Queue的多进程售票系统

```python
from multiprocessing import Process, Queueimport time
import random
from multiprocessing import Process, Queue


class Ticket:
    """票"""

    def __init__(self, ticket_no):
        # 票
        self.ticket_no = ticket_no

    def __str__(self):
        return f"{self.__class__.__name__}({self.ticket_no})"


class TicketWindow(Process):
    """售票窗口"""

    def __init__(self, name, ticket_queue: Queue):
        super().__init__(name=name)
        self.ticket_queue = ticket_queue

    def run(self):
        while self.ticket_queue.qsize() > 0:
            # 获取 票
            ticket = self.ticket_queue.get()
            print(f"窗口{self.name} 正在售票， 票号是 {ticket},  剩余票数 {self.ticket_queue.qsize()}")
            # 每售票 1张票 、延迟 0.5 ~ 2 秒
            time.sleep(random.random() * 1.5 + 0.5)

        else:
            print(f"窗口{self.name} 已售罄 ！！！")


if __name__ == '__main__':
    # 创建一个窗口窗口， 并初始化 100张票
    ticket_list = [Ticket(x) for x in range(1, 101)]

    # 创建一个队列
    queue = Queue(maxsize=100)
    # 向队列中 添加数据 使用
    for ticket in ticket_list:
        queue.pu(ticket)

    for x in range(1, 5):
        ticket_window = TicketWindow(f"窗口-{x}", queue).start()

```

**上述系统 可能会导致 并发问题**

## 锁 机制 

在 多进程/多线程 中，如果在并行执行任务的时候， 争抢 同一个资源，那么这个 资源被称为 临界资源 。这个临界资源 可能会产生并发问题。

如果要解决 并发带来的问题， 可以采用 加锁 的方式 

`from multiprocessing import Lock,   RLock `  ， 锁 主要有 2个方法 acquire (添加锁) 、 release （释放锁）

- Lock  :   互斥锁 
- RLock  :  可重入锁

## 基于锁的多进程售票系统

```python
import time
import random
from multiprocessing import Process, Queue, Lock


class Ticket:
    """票"""

    def __init__(self, ticket_no):
        # 票
        self.ticket_no = ticket_no

    def __str__(self):
        return f"{self.__class__.__name__}({self.ticket_no})"


class TicketWindow(Process):
    """售票窗口"""

    def __init__(self, name, ticket_queue: Queue, lock: Lock):
        super().__init__(name=name)
        self.ticket_queue = ticket_queue
        self.lock = lock

    def run(self):

        while self.ticket_queue.qsize() > 0:
            # 每售票 1张票 、延迟 0.5 ~ 2 秒
            # time.sleep(random.random() * 1.5 + 0.5)
            with self.lock:
                if self.ticket_queue.qsize() > 0:
                    # 获取 票
                    ticket = self.ticket_queue.get()
                    print(f"窗口{self.name} 正在售票， 票号是 {ticket},  剩余票数 {self.ticket_queue.qsize()}")

        else:
            print(f"窗口{self.name} 已售罄 ！！！")


if __name__ == '__main__':
    # 创建一个窗口窗口， 并初始化 100张票
    ticket_list = [Ticket(x) for x in range(1, 101)]

    # 创建一个队列
    queue = Queue()
   
    for ticket in ticket_list:
        queue.put_nowait(ticket)

    # 创建一把 互斥锁
    lock = Lock()

    for x in range(1, 5):
        ticket_window = TicketWindow(f"窗口-{x}", queue, lock).start()

```

## RLock 的使用方式

```python
from multiprocessing import Process, Lock, RLock


def task(lock):
    print("task------------------")
    with lock:
        test(lock)


def test(lock):
    with lock:
        print("test----------")


if __name__ == '__main__':
    lock = RLock()

    Process(target=task, args=(lock,)).start()

```

## join() 方法

当 某个 线程/进程 调用 join 的时候， 会 阻塞 当前所在的线程/进程、 直到 这个 线程/进程 执行完毕后，被阻塞的线程/进程 才会继续执行。

```python
def task():
    print(f"{current_process().name} 正在执行任务....")


if __name__ == '__main__':

    # 定义一个空的列表，用来存储多个子进程对象
    pls = []

    # 创建 5个进程
    for x in range(5):
        p = Process(target=task)
        # 启动 进程
        p.start()
        pls.append(p)

    # 希望 下面的代码 在所有 子进程执行完毕后才执行
    # 遍历 进程列表
    for p in pls:
        # join 加入当前进程(主进程)、并阻塞当前进程、等待 p 这个进程 执行完毕后 才继续执行 当前进程
        p.join()

    print("over !!!!")
```

## 死锁

死锁是指在多线程或多进程编程中，多个线程或进程因争夺资源而相互等待，导致它们永远无法继续执行下去的情况。

死锁的四个必要条件：

互斥条件：至少有一个资源必须处于“非共享”模式，即某个资源一次只能被一个进程使用。

占有并等待：至少有一个进程持有一个资源，并等待其他进程持有的资源。

非抢占条件：已分配给一个进程的资源，在该进程使用完之前，不能强行剥夺。

循环等待条件：存在一种进程资源的循环等待关系，即进程 A 等待 B 持有的资源，B 等待 C 持有的资源，C 等待 A 持有的资源，形成一个闭环。

## 死锁的解决方案

死锁预防试图通过打破死锁的四个必要条件中的至少一个来避免死锁。

打破互斥条件：将某些资源设置为共享资源。适用于只读资源。

打破占有并等待条件：进程在请求资源时，必须先释放已持有的所有资源。例如，进程 A 请求 R2 之前，必须释放 R1。

打破非抢占条件：如果进程已经持有一些资源并且无法继续执行（比如它等待资源的其他进程），系统可以强制回收该进程持有的资源，并分配给其他进程。

打破循环等待条件：资源请求的顺序应当固定，保证资源的请求顺序不形成环。例如，要求进程按顺序申请资源：R1、R2、R3。

# 多线程

- 使用 面向过程的 方式 创建 多线程 
  ```python
  from threading import Thread
  
  
  def execute_task():
      print("我是一个子线程执行的任务")
  
  
  if __name__ == '__main__':
      # 创建一个 线程对象
      thread = Thread(target=execute_task)
  
      thread.start()
  
      print("主线程结束")
  
  ```
- 使用 面向对象的 方式 创建多线程 
  ```python
  from threading import Thread
  
  
  class MyThread(Thread):
  
      def run(self):
          print("我是一个子线程执行的任务")
  
  
  if __name__ == '__main__':
      # 创建一个 线程对象
      thread = MyThread()
  
      thread.start()
  
      print("主线程结束")
  
  ```

## 线程事件对象

> 线程事件对象 threading.Event :  可以实现 让 一个线程 通知 另一个线程 终止任务。事件对象是 线程安全的，不需要考虑 加锁

- 创建一个事件对象

```
event = threading.Event()
```

- 触发事件

```
event.set()
```

- 判断是否触发事件

```
event.is_set()
```

## 龟兔赛跑

```python
from abc import ABC , abstractmethod
from threading import Thread, Event
import time 

class Animal(Thread, ABC):
    # 定义一个类属性，用来标记游戏场地的长度
    game_screen_length = None 

    def __init__(self, name, speed, time=0, state=False, *, event: Event):
        """
        :param speed : 速度
        :param name :  动物的名字
        :param time  : 时间
        :param state : 是否到达终点   
        """
        super().__init__(name=name)
        self.speed = speed 
        self.time = time 
        self.state = state 
        self.stop_event = event 

    @abstractmethod
    def distance(self):
        """
        计算距离
        """
        pass 

    def run(self) -> None:
        while not self.stop_event.is_set():
            # 让时间增加 0.1秒
            self.time += 0.1
            # 获取 0.1秒 经过的记录 
            length = round(self.distance())
            print(f"{self.name}在{self.time:.1f}秒跑了{length}毫米") 
            if length >= self.game_screen_length:
                # 将状态设置为 结束
                self.state = True
                self.stop_event.set()
                break 
            # 睡眠 0.1 秒
            time.sleep(0.1)
    

class Turtle(Animal):
    """ 
    乌龟
    """
    def distance(self):
        return int(self.time * self.speed)
   
        
class Rabbit(Animal):

    def distance(self):
        if self.time <= 5:
            return int(self.time * self.speed)
        # 休息的三分钟内兔子跑的距离不变
        if self.time <= 185:
            return int(5 * self.speed)
        # 去掉休息的三分钟
        return int((self.time - 180) * self.speed)


if __name__ == "__main__":
    print("龟兔赛跑游戏开始....")

    # 创建一个线程事件 对象、用来通知 另一个线程 停止任务
    event = Event()

    # 设置比赛场地的长度 2000 毫米
    Animal.game_screen_length = 2000

    # 创建一个 乌龟线程 、乌龟速度 10/s , 兔子 速度 90/s
    turtle = Turtle("乌龟", 10, event=event)
    rabbit = Rabbit("兔子", 90, event=event)

    turtle.start()
    rabbit.start()
    # 阻塞主进程
    turtle.join()
    rabbit.join()
    # 输出 最终的结果 
    if turtle.state and rabbit.state:
        print("平局")
    elif turtle.state:
        print(f"乌龟胜利、比兔子多跑了 {turtle.distance() - rabbit.distance()}毫米")
    else:
        print(f"兔子胜利、比乌龟多跑了 {rabbit.distance() - turtle.distance()}毫米")
```

## 线程池

存储多个线程的容器 、 可以实现对线程的复用、减少线程的创建和销毁操作。

### 实现方式 

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread


def get_premiter(num):
    """获取素数"""
    print(f"线程{current_thread().name} 正在执行任务 .....")
    for x in range(2, int(num ** 0.5 + 1)):
        if num % x == 0:
            break 
    else:
        return num
        

if __name__ == "__main__":
    # 创建一个 线程池 执行器、并设置 线程个数
    executor = ThreadPoolExecutor(10)

    # 使用 10个线程 将任务 执行 10000 次 
    futures = [executor.submit(get_premiter, n) for n in range(2, 10000)]
    
    result = []
    # 使用 as_completed 函数 获取未来结果
    for f in as_completed(futures):
        # 获取 每一个 futuers 返回的结果
        if f.result() is not None:
            result.append(f.result())
            
    # 对计算的结果进行排序
    print(sorted(result))
```