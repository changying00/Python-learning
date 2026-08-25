from  threading import Semaphore,Thread
import time
semaphore = Semaphore(3)  # 创建一个计数信号量，初始值为 3

def access_resource(name):
    with semaphore:
        print(f"{name} 进入资源区")
        #模拟处理
        time.sleep(1)
        print(f"{name}离开资源区")

threads = [Thread(target= access_resource,args= (f"T{i}",)) for  i in range(6)]

for t in threads: t.start()
for t in threads: t.join()