#【装饰器】编写一个装饰器 cache_decorator，它可以缓存函数的计算结果。如果相同的参数再次传递给函数，它应该返回缓存的结果，而不再计算。
#定义装饰器
def cache_decorator(func):
    #定义一个字典、用来缓存计算结果
    cache ={}
    #定义一个包装函数
    def wrapper(*args, **kwargs):
        #将参数作为字典的键
        key =(args,tuple(kwargs.values()))
        #如果参数已经计算过
        if key in cache:
            print("从缓存种获取结果")
            return cache[key]
        #第一次计算
        print("正在计算。。。")
        result =  func(*args, **kwargs)

        #将结果保存到缓存
        cache[key] = result

        #返回结果
        return result
    return wrapper

@cache_decorator
def add(a,b):
    print("执行add()函数")
    return a+b

print(add(10, 20))
print("-" * 30)

print(add(10, 20))
print("-" * 30)