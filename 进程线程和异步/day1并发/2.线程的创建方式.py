from threading import Thread
#方式1：传入callable(简单任务)
def task1(name):
    print(f"Task1 {name} is running...")
t1 = Thread(target=task1, args=("A",))
t1.start()  
t1.join()   # 等待线程结束


#方式2：继承Thread类(复杂任务)
class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"MyThread {self.name} is running...")

t2 = MyThread("B")
t2.start()
t2.join()  # 等待线程结束
"""
 threading.Thread API 速查
参数	类型	说明
target	callable	线程要执行的函数
args	tuple	target 的位置参数
kwargs	dict	target 的关键字参数
name	str	线程名称（默认 Thread-N）
daemon	bool	是否为守护线程
方法	说明
start()	启动线程
join(timeout)	等待线程结束
is_alive()	检查线程是否仍在运行
name	线程名称（读写）
ident	线程 ID（整数）
daemon	是否守护线程（读写
"""