"""
    多线程 : 

        a) 基于 面向过程 的 实现方式 

        b) 基于 面向对象 的 实现方式

Thread(group=None, target=None, name=None, args=(), kwargs=None,  *, daemon=None):

    target :  线程用来执行任务的 函数 
    name : 设置 线程的名字 、默认名是 Thread-N , N 是一个线程
    args :  给 线程执行任务的 函数 设置 位置参数
    kwargs: 给 线程执行任务的 函数 设置 关键参数

    daemon: 是否将 线程 做成 守护线程。

"""
from threading import Thread 
import time 


# def execute_task(name):
#     # 当 子线程 进入睡眠状态的时候、他叫 交出 CPU的执行权限 
#     time.sleep(0.01)
#     print("我是子线程、用来执行任务....")
#     pass


# # 通过 面向过程的方式 实现 多线程 
# if __name__ == "__main__":
    
#     # 定义一个变量 
#     name = "张三"
#     # 创建一个线程对象 
#     thread = Thread(target=execute_task, args=(name, ))

#     # 启动 子线程 、不代表 会 立即执行 子线程中 任务 
#     # 线程 要不要 执行 、主要 是 靠 CPU 给 线程分配的 时间片 (时间间隔) 决定的 
#     thread.start()

#     print("我是主线程、用来执行主要任务~~~~")


class MyThread(Thread):
    """
    创建一个类 、继承 Thread 类 、并 重写 父类中的 run 方法
    """
    def __init__(self, name, a):
        super().__init__(name=name)
        self.a = a 

    def run(self):
        
        print(f"我是一个子线程， 用来执行任务, 我的参数是 {self.a}")


if __name__ == "__main__":
    
    # 创建一个 线程对象 
    thread = MyThread("test", 10)

    # 调用 start 方法 启动线程 
    thread.start()

    print("我是主线程、用来执行主要任务~~~~")
