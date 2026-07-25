"""
【装饰器】编写一个装饰器 cache_decorator(timer)，
它可以缓存函数的计算结果、并将结果存储 timer 秒。如果在 timer 秒内 相同的参数再次传递给函数，
它应该返回缓存的结果，而不再计算。
"""
#导入需要的库
import time

#定义一个带参数的装饰器
def cache_decorator(timer):
   #第一层、接收被装饰的函数
    def decorator(func):
        # 定义一个字典、用于保存缓存
        """
        格式:
        {    参数:(计算结果，保存时间)}
        """
        cache = {}
        #第二层:包装函数
        def wrapper(*args, **kwargs):
            #将参数作为字典的键
            key = (args,tuple(kwargs.items()))
            #获取当前的时间
            current_time = time.time()
            #如果缓存中已经存在该参数
            if key in cache:
                #取出缓存结果和保存的时间
                result,save_time  = cache[key]
                if current_time - save_time <= timer:
                    print("读取缓存结果")
                    #没有过期、直接换回缓存
                    return result
            #没有缓存、或缓存已经过期
            print("正在计算")
            #调用原函数
            result = func(*args, **kwargs)
            #保存新的缓存
            cache[key] = (result,current_time)
            #返回结果
            return result
        #返回包装函数
        return wrapper
    #返回装饰器
    return decorator






#原函数
@cache_decorator(timer = 3)
def add(a,b):
    print("执行 add()")
    return a+b

#第一次调用
print(add(10, 20))
#第二次调用直接读取缓存结果
print(add(10, 20))

# 等待4秒，让缓存失效
time.sleep(4)
print(add(10, 20))