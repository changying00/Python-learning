"""
装饰器 编写步骤:
    1.定义一个外部函数、作为装饰器函数、且函数有且只有1个函数、参数代表要装饰器的目标函数对象

    2.定义一个内部函数、内部函数 参数为 *args, **kwargs,代表 目标函数需要的参数列表

    3.在内部 函数种 编写 装饰逻辑

        3.1 在目标函数前 编写增强代码（可有可无）

        3.2 调用 目标函数 并获取 函数执行的结果

        3.3 在 目标函数执行后 编写 增强代码（可有可无）

        3.4 内部函数 返回 目标函数执行的结果
    4.外部函数 返回内部函数引用、形成闭包结构
编写一个装饰器 、 将目标函数 返回的 整数结果 乘以 2
如果 在装饰器 希望 装饰的目标函数 函数名仍旧是 原来的名字、则需要在装饰器 内部函数上面 添加一个 @functools.wrap(func)
"""
import functools


def double(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 调用 目标函数 获取结果
        ret = func(*args, **kwargs)
        # 判断 ret 结果是否是 整数
        if type(ret) == int:
            return ret * 2

        # 如果 不满足条件 、返回目标函数执行的结果
        return ret

    return wrapper


@double
def sum(a, b):
    """求和"""
    return a + b


# sum 等价于  double(sum)、 sum(3, 5) 等价于 double(sum)(3, 5)
# 如果 一个函数 被装饰器 修饰了 ，那么 这么函数 会发生变化哪
print(sum,  sum.__name__)

print(sum(3, 5))