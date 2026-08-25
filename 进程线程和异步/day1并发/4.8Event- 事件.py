from threading import Thread,Event

import time

event = Event()

def waiter():
    print("等待事件...")
    event.wait() #阻塞 知道 event.set
    print("事件已发生！")

def setter():
    time.sleep(2)
    print("触发事件！")
    event.set()

t1 = Thread(target = waiter)
t2 = Thread(target = setter)
t1.start(); t2.start()
t1.join();t2.join()