from threading import Thread, Lock, RLock

"""
Lock 互斥锁 :  当一个线程 持有了这把锁 ，当它没有 释放的时候， 任何线程(包含它自己) 都无法 再次持有这个锁。

RLock 可重入锁 :  同一个 线程 可以 对 这把锁 多次 持久、 可以简单 理解为 锁上有一个计数器、每持有它一次 计数器 + 1, 每释放一次, 计数器 -1 
        直到 计数器为 0, 其它线程 才可以 持有它。

"""


def test(lock: Lock):
    print("--------------------test---------------")
    with lock:
        print("-------------lock test--------------")


def execute_task(lock: Lock):

    print("-----------------execute-task-------------------")

    with lock:
        print("-------------lock execute-task--------------")

        test(lock)

        print("------------------lock end execute-task")



if __name__ == "__main__":
    # 创建一个 锁 
    lock = RLock()

    # 创建一个线程对象 
    thread = Thread(target=execute_task, args=(lock, ))

    # 启动线程 
    thread.start()