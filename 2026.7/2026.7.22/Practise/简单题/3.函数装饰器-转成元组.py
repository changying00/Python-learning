"""
简单题 【装饰器】编写一个装饰器 tuple_result 、实现将函数的结果 进行包装处理成元组
例如 函数 返回一个 数字 3， 经过装饰器处理后返回 (3, )
     函数返回一个 "abc",  经过装饰器处理后返回 ("abc", )
     函数返回一个 [1, 2, 3]  经过装饰器处理后返回 (1, 2, 3)
     函数返回一个 (1, 2)  经过装饰器处理后返回 (1, 2)
30分钟
"""
#导入需要的模块
import functools
# 定义装饰器、将函数返回的结果包装成元组
def tuple_result(target):
    @functools.wraps(target)
    def wrapper(*args, **kwargs):
        #获取原函数的返回值
        result = target(*args, **kwargs)
        #判断result 本身就是元组、直接返回原值
        if type(result) == tuple:
            return result
        #如果返回值是列表、转换成元组
        elif type(result) == list:
            return tuple(result)
        #其他类型(数字、字符串等)
        else:
            return (result,)
    return wrapper

#测试函数、 返回传入的参数
@tuple_result
def  re_count(anyway):
    return anyway
# 测试
print(re_count(3))          # (3,)
print(re_count("abc"))      # ('abc',)
print(re_count([1, 2, 3]))  # (1, 2, 3)
print(re_count((1, 2)))     # (1, 2)