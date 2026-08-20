"""
Event : 是 多线程中 一个 标记 、它 的值 True / False

    - set() :  将标记设置为 True 

    - is_set() : 判断标记是否为 True 

    - clear() : 将标记重置为 False 


多线程】编写一个多线程、模拟龟兔赛跑的故事、 
    假设 兔子 每秒钟 跑 90 毫米、乌龟每秒钟 跑 10毫米 、 
    在 兔子跑了 5秒中后睡了 3分钟、 乌龟一直匀速行驶、赛道共长 2000毫米。 
    输出最后谁胜利了, 每间隔 0.1 秒 显示 2 者 跑的距离 ！！！ 

"""
from threading import Event, Thread 
from abc import ABC, abstractmethod
import time 


class Animal(Thread, ABC):
    """
    动物类
    """
    # 设置游戏的场地的长度  距离
    game_screen_length = None

    def __init__(self, name, event: Event):
        if self.__class__.game_screen_length is None:
            raise Exception("game_screen_length 值不允许为 空")
        super().__init__(name=name)
        self.event = event

    @abstractmethod
    def distance(self, times):
        """计算在指定时间内经过的长度"""
        pass

    def run(self):
        """编写线程核心的任务执行方法"""
        # 定义一个变量、用来表示 经过的 时间 
        duration = 0
        # 每间隔 0.1s 输出 动物 跑过的 距离
        while not self.event.is_set():
            # 延迟 0.1 输出结果 
            time.sleep(0.1)
            duration += 0.1 
            # 获取 duration 时长 经过的 距离 
            length = self.distance(duration) 
            # 输出 length 
            print(f"{self.name} 在 {duration:.1f}秒 跑了{length:.1f}毫米") 
            # 如果 length 超出了 场地的长度 
            if length >= self.__class__.game_screen_length:
                print(f"{self.name} 胜利")
                # 通知 另一个 动物 停止比赛 
                self.event.set()


class Rabbit(Animal):

    def __init__(self, name, speed, event):
        super().__init__(name, event)
        self.speed = speed 

    def distance(self, times):
        # 兔子跑了 5秒 中后睡了 3分钟
        if times <= 5:
            return self.speed * times 

        if times <= 3 * 60 + 5:
            return self.speed * 5 

        return self.speed * (times - 3 * 60)


class Turtle(Animal):

    def __init__(self, name, speed, event):
        super().__init__(name, event)
        self.speed = speed 

    def distance(self, times):
        return self.speed * times


if __name__ == "__main__":
    
    # 创建一个 事件对象 
    event = Event()

    # 设置 游戏的场地 
    Animal.game_screen_length = 2000

    # 创建 一个 兔子 和 一个 乌龟 
    rabbit = Rabbit("兔子", 90, event)
    turtle = Turtle("乌龟", 10, event)

    # 开始比赛 
    rabbit.start()
    turtle.start()

