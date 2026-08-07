"""

基于 类 的装饰器

__init__ :   (外部函数)

__call__ :   将一个对象 做成 可调用的 ...  (内部函数)


如果 要 定义一个 带 参数的 装饰器 、需要 三层嵌套

__init__ :  最外层函数

__call__ :  第二层函数

在 __call__ 嵌套一个 函数 作为 第三层 函数



"""
import time


class Timer:

    def __init__(self, func):
        self.__func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        # 获取 当前 时间戳
        start = time.time()
        # 调用 目标函数 并获取执行的结果
        ret = self.__func(*args, **kwargs)
        # 获取 当前 时间戳
        end = time.time()
        # 输出 目标函数执行的时长
        print(f"目标函数 {self.__func.__name__} 执行共消耗 {end - start:.2f} 秒")
        return ret

    def __str__(self) -> str:
        return str(self.__func)


class Zoom:
    """
    将 目标函数的 运行结果 放大 n 倍
    """

    def __init__(self, n):
        self._n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 执行 目标函数
            ret = func(*args, **kwargs)

            if isinstance(ret, (int, float)):
                return ret * self._n

            return ret

        return wrapper


@Zoom(5)
@Timer
def sum(a, b):
    return a + b


if __name__ == "__main__":
    print(sum(1, 2), sum)

    # a = A()
    # A(func)(*args, **kwargs)
    # 当 对 一个 对象 进行调用的时候，会 自动 执行 __call__ 魔术方法
    # print(a())

    # A(func)(*args, **kwargs)