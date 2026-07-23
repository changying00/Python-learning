"""
【装饰器】编写一个装饰器 pow(n=1) 可以将 返回 int 类型的函数的结果 改变为 n次幂。
例如 返回 2，则经过装饰器 pow(n=4)后， 函数返回结果为 16
"""
from functools import wraps
#定义 一个带参数的装饰器
def power(n= 1):
    """
    将被装饰的函数的返回值变为 n次幂
    :param n: 幂次、默认值为1
    """
    #中间的函数、接收被装饰的函数
    def decorator(func):
        #wraps 用来保留原函数的函数名，注释等信息
        @wraps(func)
        def wrapper(*args, **kwargs):
            #调用原函数、得到返回值
            result = func(*args, **kwargs)
            #将返回值进行 n 次幂运算
            return result ** n
        return wrapper
    return decorator

# 使用装饰器、将返回值变为 4次幂
@power(4)
def get_number(n):
    return n
# 2的4次幂 =16
print(get_number(2))
"""
执行过程

@power(4) 先执行，得到一个装饰器函数 decorator。

decorator 接收被装饰的函数 get_number。

调用 get_number() 时，实际上执行的是 wrapper()。

wrapper() 内部先调用原函数，得到 2。

再执行 2 ** 4，结果为 16。

带参数装饰器的固定模板是：

def 外层(参数):
    def 中层(func):
        def 内层(*args, **kwargs):
            return func(*args, **kwargs)
        return 内层
    return 中层
"""