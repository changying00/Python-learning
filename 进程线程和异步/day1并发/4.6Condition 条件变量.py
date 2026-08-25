from threading import Thread,Condition
import time
items = []
condition = Condition()

def producer():
    with condition:
        items.append("item")
        print("生产了 item")
        condition.notify()#通知消费

def consumer():
    with condition:
        while not items:
            print("没有 item，等待生产")
            condition.wait()#等待生产者通知
        item = items.pop()
        print(f"消费了 {item}")

t1 = Thread(target=consumer)
t2 = Thread(target=producer)
t1.start()
time.sleep(0.5) #确保 consumer 先运行
t2.start()

t1.join(); t2.join()
