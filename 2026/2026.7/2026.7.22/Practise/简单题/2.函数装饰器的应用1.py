#【装饰器】编写一个装饰器 timer、用来记录函数的运行时间 提示: 可以使用 time 模块中的 time() 函数 返回当前时间的时间戳(秒)

#导入time模块
import time
import functools
# 定义一个装饰器，用于统计函数运行时间
def timer(target):
    @functools.wraps(target)
    # count_time 用来保留原函数的名称和文档信息
    def count_time(*args, **kwargs):
        # 记录函数开始执行的时间
        start = time.time()
        # 执行原函数，并接收返回值
        result = target(*args, **kwargs)
        # 记录函数结束执行的时间
        end = time.time()
        # 计算并输出函数运行时长
        print(f"函数 {target.__name__} 执行时长 {end - start} 秒")
        # 返回原函数的结果，保证装饰器不改变原函数功能
        return result
    # 返回包装后的函数
    return count_time

# 使用 @timer 装饰器装饰 count 函数
@timer
def count(a,b):
    return a + b
#调用函数
print(count(3, 5))


