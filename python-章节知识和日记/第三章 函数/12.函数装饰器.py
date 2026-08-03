"""
装饰器 :  采用 闭包技术 实现的

    在 不改变 原有 函数 代码的基础上，  对函数的功能 进行 增强。

    它是一种 切面 技术 。


在 python 语言中 ，针对

    timer(sub)(3, 5) 调用, 官方 提供了一个语法糖
    只需要 在 目标函数 上方 添加一个 @timer (装饰器) 、就可以 使用 sub(3, 5) 代替 timer(sub)(3, 5) 代码



"""
import time
def timer(target):
    """记录目标函数执行时长"""
    def wrapper(*args, **kwargs):
        # 获取 目标函数执行前的 时间戳
        start = time.time()
        # 执行 目标函数 、并获取 结果
        ret = target(*args, **kwargs)
        # 获取 函数任务 执行后的 结束时间
        end = time.time()
        print(f"函数 {target.__name__} 执行时长 {end - start} 秒")
        # 返回 目标函数执行的结果
        return ret

    return wrapper
# def sum(a, b):
#     # 获取 函数 任务 执行前 的 开始时间
#     start = time.time()
#     c = a + b
#     # 获取 函数任务 执行后的 结束时间
#     end = time.time()
#     print(f"函数 sum 执行时长 {end - start} 秒")
#     return c
@timer
def sub(a, b):
    return a - b

@timer
def mul(a, b):
    return a * b

@timer
def div(a, b):
    return a / b

@timer
def pow(a, b):
    return a ** b
# print(sum(1, 10))
# 统计 sub 函数执行的时长
# print(timer(sub)(3, 5))
print(sub(3, 5))
print(mul(3, 6))
