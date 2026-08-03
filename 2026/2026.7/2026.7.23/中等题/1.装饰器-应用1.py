"""
【装饰器】编写一个装饰器 add_int_num(num=0) 、将所有返回 整数的函数 结果 增加 num
"""
#导入相关的库
import functools
#定义一个装饰器使将返回的整数结果增加 num
def add_int_num(num = 0):
     def decorator(func):
        #把原函数的名字不变
        @functools.wraps(func)
            # 定义一个内部函数
        def wrapper(*args,**kwargs):
               #接收函数返回的值
            result =func(*args,**kwargs)
            if isinstance(result, int):
                return result + num
            return result
        return wrapper
     return decorator
#原函数将传入的整数返回
@add_int_num(5)
def int_num(num = 0):
    return  num

if __name__ == '__main__':
    print(int_num(2))