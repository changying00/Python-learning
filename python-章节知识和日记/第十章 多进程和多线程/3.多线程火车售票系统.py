"""
多线程 共享 同一个 进程中的 数据
"""
from typing import List
import time, random 
from threading import Thread
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
    def __init__(self, name, tickets: List[Ticket]):
        self.tickets = tickets 
        super().__init__(name=name)

    def run(self):
        """
        售票
        """ 
        # 定义一个 循环 
        while len(self.tickets) > 0:
            # 获取 列表中的第一章票 
            ticket = self.tickets[0]
            # 延迟 0.5 ~ 1 秒钟 
            # time.sleep(random.uniform(0.5, 1))
            # 输出 票的 信息 
            print(f"窗口【{self.name}】正在售票、票号是 {ticket.num}、还剩余 {len(self.tickets) - 1} 张")
            # 移除 售出的 票 
            self.tickets.pop(0)
            print(f"窗口【{self.name}】票已售出、票信息 {ticket}")
        print(f"窗口【{self.name}】票已售罄")
if __name__ == "__main__":
    
    # 生成 100 张票 
    tickets = [Ticket(f"No.{x:0>4}") for x in range(1, 101)]

    # 创建一个 售票窗口 
    window = TicketWindow("郑州东站 A 窗口", tickets)

    # 模拟 售票 
    window.start()

    # 创建一个 售票窗口 
    window2 = TicketWindow("郑州东站 B 窗口", tickets)
    # 模拟 售票 
    window2.start()


    # 创建一个 售票窗口 
    window3 = TicketWindow("郑州东站 C 窗口", tickets)
    # 模拟 售票 
    window3.start()

