"""
睡眠排序法 :  采用 多线程 +  time.sleep 配合实现 ~~

"""
from threading import Thread 
import time 


def sleep_sort(val, array):
    # 睡眠 、在 val 秒 后 会自动 睡醒 
    time.sleep(val)
    # 将 数据 添加 到 array 列表中 
    array.append(val)
    print(val)


# 定义一个 要排序的列表
ls = [3, 16, 8, 1, 6, 19]

# 定义一个 空列表 、用来存储 排序后的数据 
new_ls = [] 

# 定义一个 容器，存储所有的线程 
thread_pools = []
# 使用 循环 开启 多个线程 
for v in ls:
    # 开启 线程 
    thread = Thread(target=sleep_sort,  args=(v, new_ls)) 
    thread_pools.append(thread)
    # 启动 线程
    thread.start()


for t in thread_pools:
    # 阻塞 主线程 、等待 所有的 线程 睡醒
    t.join()

# 如果 for 结果、说明 所有线程 睡醒了, 输出 已经排序好的数据
print(new_ls)



