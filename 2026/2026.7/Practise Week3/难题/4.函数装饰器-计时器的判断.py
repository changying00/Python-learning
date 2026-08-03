"""
【装饰器】编写一个 func_rate(*, duration=60, count=1) 装饰器、可以实现 函数调用限流操作 、
例如 @func_rate(duration=60, count=10)
代表目标函数在一分钟内只允许访问10次 提示： 需要记录第一次访问的时间 (time.time())
"""
import time
#定义带参数的装饰器
def func_rate(*,duration=60, count=1):
    #第一层接收被装饰的参数
    def decorator(func):
        #第一次调用的时间
        first_time= 0
        #当前时间段内已经调用的次数
        call_count = 0
        # 第二层:包装函数
        def wrapper(*args, **kwargs):
            #使用nonlocal 修改外层变量
            nonlocal first_time,call_count
            #获取当前时间
            current_time = time.time()
            #第一次调用
            if first_time == 0:
                first_time = current_time
            #判断是否已经超过了限制时间
            if current_time - first_time > duration:
                    #超过限制时间、重新开始统计
                    first_time = current_time
                    call_count = 0
            # 判断调用次数是否超过限制
            if call_count >= count:
                print('函数调用次数超过限制!')
                return
            #次数加1
            call_count += 1
            print(f"第{call_count}次调用")
            #执行原函数
            return func(*args, **kwargs)
        #返回包装函数
        return wrapper
    #返回装饰器
    return decorator
@func_rate(duration=5, count=3)
def add(a, b):
    print(f"计算：{a} + {b}")
    return a + b
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))
# 第四次，超过限制
print(add(7, 8))

print("等待6秒......")
time.sleep(6)
# 时间窗口重置，可以重新调用
print(add(10, 20))