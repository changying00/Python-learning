"""
   你的总结：
    消费型函数：有参数，但没有返回值。
    定义一个 each 函数，实现消费可迭代对象中的每一个数据。
我的解释：
    消费型函数的重点是“处理数据”，而不是“计算并返回结果”。
    它通常接收一个或多个参数，在函数内部完成某种操作，最后不需要 return 返回值。
    在 Python 中，如果函数没有写 return，默认返回 None。

    each(iterable, consumer) 这个函数中：
        iterable 表示可迭代对象，例如列表、元组、字符串等。
        consumer 表示消费函数，负责处理 iterable 中的每一个数据。

    each 函数本身不关心每个数据具体怎么处理，
    它只负责遍历 iterable，然后把每一个元素交给 consumer 去消费。
    这样做的好处是：
        遍历逻辑和处理逻辑分离。
        想打印数据，就传入打印函数。
        想发送短信，就传入发送短信的函数
"""

def each(iterable, consumer):
    """ 消费可迭代对象中的每一个数据"""

    for v in iterable:
        #消费每一个数据
        consumer(v)
#使用 each 函数 打印列表中的 每一个元素
ls = [23,56,22,33,31]
each(ls ,lambda x : print(x))
#使用 each 函数 将列表中的每一个数据 发给 手机号为133 0370 1853 的用户
each(ls ,lambda x : print(f"正在向手机号133 0370 1853 的用户发送短信{x}"))