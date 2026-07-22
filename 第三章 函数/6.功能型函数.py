"""
功能型函数:  既有参数、 又用返回值 ~~~

1.  定义一个 计算函数 、实现 2个数字的运算 !!!

2.  编写一个 map 函数 、将 可迭代对象中的 数据 进行映射 并返回一个新的列表

例如 将 一个 列表 [1, 2, 3]  通过 map 映射后 变成 [1, 4, 9] ,   或者 变成 [1, 3, 5]

"""
from typing import Callable, Iterable, Any, Union


def calc(a: Union[int, float], b: Union[int, float],
         functional: Callable[[Union[int, float], Union[int, float]], Union[int, float]]) -> Union[int, float]:
    """实现 2 个数字的运算 、并返回运算后的结果 """
    return functional(a, b)


def map(iterable: Iterable[Any], functional: Callable[[Any], Any]):
    """将可迭代对象中的数据 进行映射、 并返回一个 新的列表"""
    return [functional(v) for v in iterable]


# 使用 calc 函数 实现 3 和 5 加法运算
print(calc(3, 5, lambda x, y: x + y))

# 使用 calc 函数 实现 计算 3 的 5 次幂
print(calc(3, 5, lambda x, y: x ** y))

ls = [12, 34, 7, 6]
# 使用 map 函数 、将 列表中的元素 扩大 10倍
print(map(ls, lambda d: d * 10))
# 使用 map 函数 、将 别表中的 每一个元素 获取 它的平方
print(map(ls, lambda d: d ** 2))
# 使用 map 函数 将 列表中的每一个元素 扩大 2 倍后 -1
print(map(ls, lambda d: d * 2 - 1))