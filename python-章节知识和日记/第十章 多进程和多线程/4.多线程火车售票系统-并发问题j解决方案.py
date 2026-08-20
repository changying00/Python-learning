"""
多线程 共享 同一个 进程中的 数据 

并发:  在 同一个时刻 、由 多个线程 争抢 同一个资源 、最后产生 问题 。

多线程 售票 可能会存在 超卖、 卖重 等现象 

解决方案 :  将 临界资源的操作 做成 原子 操作 ,  线程中 提供了 锁机制、 锁可以让 某一段代码 做成原子操作

原子操作 : 不可再分、 只有持有锁的 线程 才能 执行 原子操作 , CPU 在 原子操作中 不会 释放锁 、

Lock 锁 :
    a)  acquire() : 获取锁 

    b)  release() : 释放锁
"""
from typing import List
import time, random 
from threading import Thread, Lock
class Ticket:
    """
    火车票 
    """
    def __init__(self, num):
        self.num = num 

    def __repr__(self):
        return f"{self.__class__.__name__}({self.num})"
class TicketWindow(Thread):
    """
    售票窗口
    """
    def __init__(self, name, tickets: List[Ticket], lock: Lock):
        self.tickets = tickets 
        self.lock = lock 
        super().__init__(name=name)
    def run(self):
        """
        售票
        """ 
        # 定义一个 循环 
        while len(self.tickets) > 0:
            # 延迟 0.5 ~ 1 秒钟 
            time.sleep(random.uniform(0.5, 1))

            with self.lock:
                if len(self.tickets) > 0:
                    # 获取 列表中的第一章票 
                    ticket = self.tickets[0]
                    # 移除 售出的 票 
                    self.tickets.pop(0)
                else:
                    break 
            # 输出 票的 信息 
            print(f"窗口【{self.name}】正在售票、票号是 {ticket.num}、还剩余 {len(self.tickets)} 张")
            # 延迟 0.5 ~ 1 秒钟 
            #time.sleep(random.uniform(0.5, 1))
            print(f"窗口【{self.name}】票已售出、票信息 {ticket}")
        print(f"窗口【{self.name}】票已售罄")
if __name__ == "__main__":

    # 创建一个 锁对象、用来控制 临界资源 操作 、将 某些操作 做成原子操作 
    lock = Lock()
    
    # 生成 100 张票 
    tickets = [Ticket(f"No.{x:0>4}") for x in range(1, 101)]

    # 创建一个 售票窗口 
    window = TicketWindow("郑州东站 A 窗口", tickets, lock)

    # 模拟 售票 
    window.start()

    # 创建一个 售票窗口 
    window2 = TicketWindow("郑州东站 B 窗口", tickets, lock)
    # 模拟 售票 
    window2.start()

    # 创建一个 售票窗口 
    window3 = TicketWindow("郑州东站 C 窗口", tickets, lock)
    # 模拟 售票 
    window3.start()

