#【装饰器】编写一个装饰器 logs、记录函数的执行信息、包括 函数名、参数、返回值结果
#导入相关模块
import functools
#定义装饰器 log是用于记录函数的执行信息、包含函数名、参数、返回值
def logs(func):
    @functools.wraps(func)
    #定义wrapper内部函数
    def wrapper(*args,**kwargs):
        #定义一个变量result 用于接收func函数的值
        result= func(*args,**kwargs)
        #记录函数执行的信息包括 函数名字、参数、返回值结果
        print(f"函数名：{func.__name__}")
        print(f"位置参数：{args}")
        print(f"关键字参数：{kwargs}")
        print(f"返回值：{result}")
        #返回值
        return result

    return wrapper

#测试函数
@logs
def sum_num(a,b):
    return a+b
#测试结果
print(sum_num(3,4))
print(sum_num(3,b = 8))
print(sum_num(a= 13,b = 28))